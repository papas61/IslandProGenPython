# 🏝 IslandProGen

IslandProGen is a desktop AI application built with Tkinter that generates creative island concepts and automatically creates AI-generated images based on those ideas.

The app uses OpenAI for:
- Text generation (creative island ideas)
- Image generation (AI-created visuals)

---

## ✨ Features

- Generate 2 or 3 creative island ideas from a custom prompt
- Automatically create 1024x1024 AI images
- Browse images using keyboard arrows (← →)
- Preview the first generated image externally
- Dark themed UI using ttkthemes
- Images saved locally in an `outputs/` folder

---

## 🛠 Requirements

Install dependencies:

```bash
pip install openai pillow ttkthemes
```

You also need:
- Python 3.9+
- A valid OpenAI API key

---

## 🔑 API Key Setup (Direct in Code)

Open your Python file and replace:

```python
client = openai.OpenAI(api_key='sk-proj-')
```

with:

```python
client = openai.OpenAI(api_key='your_real_key_here')
```

⚠ Keep your API key private. Do not upload it to GitHub or share it publicly.

---

## ▶ How To Run

```bash
python ImageGenerator.py
```

---

## 🎮 How To Use

1. Choose generation mode:
   - **Short** → 2 island ideas
   - **Extended** → 3 island ideas
2. Enter a theme (example: `ancient floating crystal kingdom`)
3. Click **Enter**
4. Wait for ideas and images to generate
5. Use:
   - ← Arrow Key → Previous image
   - → Arrow Key → Next image
6. Click **Preview** to open the first image externally

---

## 📂 Output

Generated images are saved automatically inside:

```
outputs/
```

File names:

```
request_1.jpg
request_2.jpg
request_3.jpg
```

---

## ⚙ Technologies Used

- Tkinter (GUI)
- ttkthemes (UI styling)
- Pillow (image handling)
- OpenAI API (text + image generation)

---

## ⚠ Notes

- Image generation may take several seconds per image.
- Make sure your API key is valid and has available credits.
- Ensure the `outputs/` directory exists or is created automatically.
- The font is called "Monocraft" for the title.

---

## 📜 License

This project is for educational and experimental purposes.

<img width="630" height="1030" alt="image" src="https://github.com/user-attachments/assets/de320940-80ea-4730-9e04-c7a89ddd03d2" />

