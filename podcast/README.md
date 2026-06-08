# Statnice na uši - audio podcast

Přehledový podcast k bakalářským státnicím (Informatika / UI / Strojové učení),
dva moderátoři (Mára = klidný expert, Terka = studentka ve stresu). Pokrývá všechny
zkouškové okruhy intuitivně, mimo-rozsahové věci vynechává. Slouží k poslechu cestou,
ne jako náhrada textu.

## Soubory
- `script.md` - scénář (math psaná slovy, aby šla číst nahlas).
- `generate.py` - vyrobí audio přes OpenAI TTS (model `gpt-4o-mini-tts`) + ffmpeg.
- `audio/kapitola-01.mp3` ... `kapitola-06.mp3` - jednotlivé kapitoly.
- `audio/statnice-podcast.mp3` - celý podcast.

## Kapitoly
1. Jak na to a proč se nebát (formát zkoušky, strategie)
2. Společná matematika (analýza, lin. algebra, diskrétní, grafy, pravděpodobnost, logika)
3. Společná informatika (automaty, složitost, algoritmy, C#, architektura/OS)
4. Základy umělé inteligence (prohledávání, CSP, Bayes sítě, HMM, MDP, hry)
5. Strojové učení (regrese, SVM, stromy, ensembly, k-means/PCA, metriky)
6. Poslední rady před zkouškou

## Regenerace
```bash
export OPENAI_API_KEY=...        # potřeba klíč
python3 podcast/generate.py
```
Hlasy: Mára = `ash`, Terka = `coral` (lze změnit v `generate.py`).

## Lepší kvalita (volitelně)
OpenAI TTS je tu nejlepší dostupná volba. Pro ještě přirozenější češtinu/podcast:
- ElevenLabs (multilingual v2) - nejlepší prozodie, potřeba ELEVENLABS_API_KEY.
- Google NotebookLM / Gemini 2.5 TTS - nativní dvouhlasý "podcast" režim.
