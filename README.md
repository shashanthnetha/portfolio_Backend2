# Shashanth Pittala — Personal Portfolio

An interactive, high-performance portfolio featuring an authored **Cinematic CRT** entry countdown and a mouse-reactive **3D WebGL Studio** showcasing production AI systems, distributed protocols, and machine learning pipelines.

🌐 **Live Demo**: [Deploy with Vercel / Cloudflare Pages]  
👨‍💻 **Developer**: [Shashanth Pittala (shashanthnetha)](https://github.com/shashanthnetha)

---

## ⚡ Key Highlights & Features

- **Cinematic CRT Loading Sequence**:
  - Full-screen WebGL + Canvas 2D authentic cathode tube simulation.
  - Classic Academy film leader with sweeping countdown dial (5 → 1), 24fps running timecode, barrel curvature distortion, scanlines, aperture grille triads, and phosphor halation bloom.
  - Seamless phosphor flash transition into the 3D portfolio with automatic WebGL disposal (`renderer.dispose()`) for zero runtime GPU overhead.
- **Interactive 3D WebGL Studio**:
  - Real-time Three.js 3D physics, mouse-reactive camera parallax, and low-latency canvas rendering.
  - Interactive **ParticleScroll** text disintegrations and state transitions.
- **Featured Projects**:
  - **Acuity Control**: Low-latency remote control system for macOS over local network socket streaming.
  - **AgriSense AI**: Multi-agent crop disease diagnosis system with Gemini 2.0 Flash Vision, ChromaDB RAG, and voice advisory.
  - **courtroom-env**: Adversarial multi-agent benchmark for legal deliberation and judicial consensus.
  - **IntelliCredit**: Financial statement parsing with Gemini Vision, Random Forest scoring, and SHAP explainability.
  - **NetWorth App**: Wealth simulator and asset projection engine with Next.js and Zustand.
  - **Analytics Shorts**: Autonomous video generation pipeline with Whisper and MoviePy.
  - **NutriLens**: On-device food safety and allergen recognition with Kotlin and ML Kit.
  - **Radius Mesh**: Off-grid decentralized P2P messaging using WiFi Direct and BLE.

---

## 🛠️ Tech Stack

- **Frontend**: React 19, TypeScript, Vite
- **3D & Shaders**: Three.js, Raw WebGL GLSL Shaders, Canvas 2D
- **Components & Effects**: Authored ThreeUI CRT Engine, ParticleScroll

---

## 🚀 Local Development

```bash
# Clone the repository
git clone https://github.com/shashanthnetha/portfolio_Backend2.git
cd portfolio_Backend2

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

---

## 📦 Deployment

### Vercel (1-Click)
1. Import repository on [vercel.com](https://vercel.com).
2. Framework Preset: **Vite**.
3. Build Command: `npm run build`.
4. Output Directory: `dist`.
5. Deploy!

### Cloudflare Pages
1. Connect repository in Cloudflare Dashboard → Workers & Pages.
2. Build preset: **Vite**.
3. Build command: `npm run build`.
4. Output directory: `dist`.
5. Deploy!
