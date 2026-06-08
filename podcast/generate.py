#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vyrobí audio podcast ze script.md pomocí OpenAI TTS (gpt-4o-mini-tts).
Dva hlasy (MÁRA / TERKA), spojeno ffmpegem po kapitolách + celý podcast.
Spuštění: OPENAI_API_KEY musí být v prostředí. python3 podcast/generate.py
"""
import os, re, json, subprocess, sys, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "script.md")
CLIPS = os.path.join(HERE, "clips")
OUT = os.path.join(HERE, "audio")
KEY = os.environ["OPENAI_API_KEY"]
MODEL = "gpt-4o-mini-tts"

VOICE = {"MÁRA": "ash", "TERKA": "coral"}
INSTR = {
    "MÁRA": "Speak Czech as a calm, witty, friendly podcast host. Natural, warm pace, "
            "light humor, explain clearly and confidently.",
    "TERKA": "Speak Czech as a curious student a bit stressed before exams. Lively, "
             "energetic, sometimes funny and slightly panicky; you ask the questions.",
}

def tts(text, voice, instr, path):
    body = json.dumps({"model": MODEL, "voice": voice, "input": text,
                       "instructions": instr, "response_format": "mp3"}).encode()
    req = urllib.request.Request(
        "https://api.openai.com/v1/audio/speech", data=body,
        headers={"Authorization": "Bearer " + KEY, "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            if len(data) < 200:
                raise RuntimeError("tiny response")
            with open(path, "wb") as f:
                f.write(data)
            return
        except Exception as e:
            if attempt == 3:
                raise
            time.sleep(2 * (attempt + 1))

def parse():
    chapters = []  # list of (title, [(speaker, text), ...])
    cur = None
    for line in open(SCRIPT, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## "):
            cur = (line[3:].strip(), [])
            chapters.append(cur)
        elif cur is not None:
            m = re.match(r"^(MÁRA|TERKA):\s*(.+)$", line)
            if m:
                cur[1].append((m.group(1), m.group(2).strip()))
    return chapters

def silence(path, secs):
    subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i",
                    "anullsrc=channel_layout=mono:sample_rate=24000",
                    "-t", str(secs), "-q:a", "9", path],
                   check=True, capture_output=True)

def concat(parts, out):
    lst = out + ".txt"
    with open(lst, "w") as f:
        for p in parts:
            f.write("file '%s'\n" % p.replace("'", "'\\''"))
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-c:a", "libmp3lame", "-b:a", "128k", out],
                   check=True, capture_output=True)
    os.remove(lst)

def main():
    os.makedirs(CLIPS, exist_ok=True); os.makedirs(OUT, exist_ok=True)
    gap = os.path.join(CLIPS, "_gap.mp3"); biggap = os.path.join(CLIPS, "_biggap.mp3")
    silence(gap, 0.35); silence(biggap, 0.8)
    chapters = parse()
    print("kapitol:", len(chapters), "replik celkem:", sum(len(c[1]) for c in chapters))
    chapter_files = []
    for ci, (title, lines) in enumerate(chapters, 1):
        parts = []
        for li, (spk, text) in enumerate(lines):
            clip = os.path.join(CLIPS, "ch%02d_%03d_%s.mp3" % (ci, li, spk))
            if not os.path.exists(clip) or os.path.getsize(clip) < 200:
                tts(text, VOICE[spk], INSTR[spk], clip)
                print("  [%d/%d] ch%d line %d (%s) %dB" %
                      (li + 1, len(lines), ci, li, spk, os.path.getsize(clip)))
            parts.append(clip); parts.append(gap)
        chf = os.path.join(OUT, "kapitola-%02d.mp3" % ci)
        concat(parts, chf)
        chapter_files.append(chf)
        print("HOTOVO kapitola %d -> %s" % (ci, chf))
    # celý podcast s většími pauzami mezi kapitolami
    full_parts = []
    for chf in chapter_files:
        full_parts.append(chf); full_parts.append(biggap)
    concat(full_parts, os.path.join(OUT, "statnice-podcast.mp3"))
    print("HOTOVO celý podcast -> audio/statnice-podcast.mp3")

if __name__ == "__main__":
    main()
