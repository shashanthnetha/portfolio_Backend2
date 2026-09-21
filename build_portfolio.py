#!/usr/bin/env python3
"""
Comprehensive portfolio builder that transforms sublevel-studio.html
into Shashanth's personal AI & Systems portfolio while preserving:
- All Three.js 3D mechanics & shaders
- VHS overlay WebGL shader
- ParticleScroll dissolve-and-reassemble text animation on scroll
- TerrainPlume canvas background
- Marginalia scroll parallax & homography
- High-tech, tactile aesthetic
"""
import re
import sys

def main():
    source_path = '/Users/netha/.gemini/antigravity-ide/scratch/sublevel-studio.html'
    target_path = '/Users/netha/.gemini/antigravity-ide/scratch/public/landing-pages/sublevel-studio.html'

    with open(source_path, 'r', encoding='utf-8') as f:
        html = f.read()

    print(f"Source size: {len(html)} bytes")

    # Verify that source contains ParticleScroll and all critical components
    assert 'mountParticleScroll' in html, "Source must contain mountParticleScroll"
    assert 'ThreeUITerrainPlume' in html, "Source must contain ThreeUITerrainPlume"
    assert 'illParallax' in html, "Source must contain illParallax"

    # 1. Document Title & Description
    html = html.replace(
        '<title>sublevel.studio | We build the stuff people remember.</title>',
        '<title>Shashanth Pittala — AI &amp; Systems Engineer</title>'
    )
    html = re.sub(
        r'<meta name="description" content="sublevel\..*?">',
        '<meta name="description" content="Personal portfolio and engineering lab of Shashanth Pittala (Sha). B.Tech AI &amp; ML at CMRCET Hyderabad. Building high-performance AI systems, multi-agent pipelines, and low-latency architectures.">',
        html
    )

    # 2. Loader & Topbar
    html = html.replace(
        '<div id="loader"><span>loading sublevel</span></div>',
        '<div id="loader"><span>loading shashanth</span></div>'
    )
    html = html.replace(
        '<a class="logo" href="#top" aria-label="sublevel.studio"><span class="wordmark">sublevel<i>.</i></span></a>',
        '<a class="logo" href="#top" aria-label="shashanth."><span class="wordmark">shashanth<i>.</i></span></a>'
    )
    html = html.replace(
        '<button class="menu-close" type="button" aria-label="Close menu"><span class="wordmark">sublevel<i>.</i></span></button>',
        '<button class="menu-close" type="button" aria-label="Close menu"><span class="wordmark">shashanth<i>.</i></span></button>'
    )
    html = html.replace(
        '<a class="active blink" href="#top">Home</a>\n      <a class="blink" href="#showcase">Work</a>\n      <a class="blink" href="#services">Services</a>\n      <a class="blink" href="#lab">Lab</a>',
        '<a class="active blink" href="#top">Home</a>\n      <a class="blink" href="#showcase">Arsenal</a>\n      <a class="blink" href="#work">Projects</a>\n      <a class="blink" href="#services">Capabilities</a>'
    )
    html = html.replace(
        '<span class="prompt">agent@sublevel</span>',
        '<span class="prompt">shashanth@system ~ $</span>'
    )
    html = html.replace(
        '<a class="icon mail blink arcade metal" href="mailto:hello@sublevel.studio" aria-label="Contact us" title="Contact us">',
        '<a class="icon mail blink arcade metal" href="mailto:shashanthnetha@gmail.com" aria-label="Contact Shashanth" title="Email: shashanthnetha@gmail.com">'
    )

    # 3. Slide-out Navigation Menu
    old_menu_links = '<a href="#top">Home</a><a href="#showcase">Work</a><a href="#services">Services</a><a href="#people">People</a><a href="#blog">Blog</a><a href="#lab">Lab</a><a href="mailto:hello@sublevel.studio">Contact</a>'
    new_menu_links = '<a href="#top">Home</a><a href="#showcase">Arsenal</a><a href="#work">Projects</a><a href="#services">Capabilities</a><a href="#people">Contact</a><a href="https://github.com/shashanthnetha" target="_blank" rel="noopener">GitHub</a><a href="https://linkedin.com/in/shashanth-pittala" target="_blank" rel="noopener">LinkedIn</a>'
    html = html.replace(old_menu_links, new_menu_links)

    old_menu_foot = '<p><b>hello@sublevel.studio</b></p>\n        <p>Kyoto &amp; remote · open late</p>\n        <p>Est. 2019 · dispatch 026</p>'
    new_menu_foot = '<p><b>shashanthnetha@gmail.com</b></p>\n        <p>Hyderabad, India · Always building</p>\n        <p>B.Tech AI &amp; ML · CMRCET</p>'
    html = html.replace(old_menu_foot, new_menu_foot)

    # 4. Hero Section
    html = html.replace(
        '<div class="eyebrow"><span>Sublevel — studio index</span><hr class="rule" data-line><span>Est. 2019</span></div>',
        '<div class="eyebrow"><span>Shashanth Pittala — Engineering Portfolio</span><hr class="rule" data-line><span>AI &amp; Systems</span></div>'
    )
    html = html.replace(
        '<h1 class="f-h0" data-ps>A digital studio &amp; brand workshop building the stuff people remember</h1>',
        '<h1 class="f-h0" data-ps>I build high-performance AI systems and real-time architectures that scale</h1>'
    )
    html = html.replace(
        '<p class="f-h4" data-ps>We team up with ambitious founders, scale-ups and brands to turn strategy into products, identities and experiences that actually ship.</p>',
        '<p class="f-h4" data-ps>Second-year B.Tech AI &amp; ML student @ CMRCET · NxtWave Fellow. Shipping full-stack LLM architectures, local-first vision inference on Apple Silicon, and high-throughput automation.</p>'
    )

    # 5. Core Technical Focus / Arsenal (Replace 12 client logos with Shashanth's exact skills)
    old_logos_pattern = r'<section class="grid-layout logos" id="showcase">.*?</section>'
    new_logos_section = '''<section class="grid-layout logos" id="showcase">
    <div class="framed label"><i class="corner tl"></i><i class="corner tr"></i><i class="corner bl"></i><i class="corner br"></i><h2 class="f-h3" data-ps>Core Technical Arsenal</h2></div>
    <hr class="rule" data-line>
    <div class="grid">
      <a href="#services" aria-label="Python"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M11.927 2c-3.13 0-5.068 1.408-5.068 3.518v2.096h5.203v.744H4.536C2.26 8.358 1 9.932 1 12.358c0 2.457 1.348 3.969 3.654 3.969h1.796v-2.227c0-2.029 1.636-3.666 3.665-3.666h5.048V7.89c0-2.262-1.928-3.89-4.236-3.89h-.002zm-1.614 1.706a1.002 1.002 0 1 1 0 2.003 1.002 1.002 0 0 1 0-2.003zM12.073 22c3.13 0 5.068-1.408 5.068-3.518v-2.096h-5.203v-.744h7.526C21.74 15.642 23 14.068 23 11.642c0-2.457-1.348-3.969-3.654-3.969h-1.796v2.227c0 2.029-1.636 3.666-3.665 3.666H8.837v2.548c0 2.262 1.928 3.89 4.236 3.89h.002zm1.614-1.706a1.002 1.002 0 1 1 0-2.003 1.002 1.002 0 0 1 0 2.003z"/></svg><span class="n">Python</span></div></div></a>
      <a href="#services" aria-label="Java"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M8.851 18.56s-.917.534.667.714c2.391.269 4.258.247 6.945-.25 0 0 .972.611 1.694.944-5.432 2.25-12.723.111-9.306-1.408zm-1.055-3.36s-1.028.75 1.139.944c2.833.25 5.583.333 9.417-.306 0 0 .639.472 1.25.806-6.445 2.11-14.778.361-11.806-1.444zm11.778 1.916s.722-.583-.694-.75c-3.194-.389-7.389-.361-10.778.222 0 0-.694-.444-1.389-.778 5.028-1.528 13.917-.417 12.861 1.306zm-1.389-5.111c1.25 1.444-.361 2.806-.361 2.806s2.306-1.167 1.25-3.083c-1.028-1.833-2.611-2.722-2.611-2.722s.917.861 1.722 3zm-3.028-4.389s2.194-1.389 1.167-3.389c0 0-.083 1.833-2.111 2.583-1.639.611-3.639 1.917-2.111 3.861 0 0 .194-.972 1.333-1.861 1.194-.944 1.722-1.194 1.722-1.194z"/></svg><span class="n">Java</span></div></div></a>
      <a href="#services" aria-label="C Systems"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm0 3.6c3.535 0 6.4 2.865 6.4 6.4 0 1.285-.38 2.484-1.033 3.488l-2.68-2.68c.075-.258.113-.528.113-.808 0-1.546-1.254-2.8-2.8-2.8s-2.8 1.254-2.8 2.8 1.254 2.8 2.8 2.8c.28 0 .55-.038.808-.113l2.68 2.68C14.484 17.02 13.285 17.4 12 17.4c-2.982 0-5.4-2.418-5.4-5.4S9.018 5.6 12 5.6z"/></svg><span class="n">C Lang</span></div></div></a>
      <a href="#services" aria-label="SQL Database"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M12 3c-4.97 0-9 1.79-9 4v10c0 2.21 4.03 4 9 4s9-1.79 9-4V7c0-2.21-4.03-4-9-4zm0 2c3.87 0 7 1.34 7 2s-3.13 2-7 2-7-1.34-7-2 3.13-2 7-2zm-7 5.23c1.61.94 4.19 1.77 7 1.77s5.39-.83 7-1.77V12c0 .66-3.13 2-7 2s-7-1.34-7-2v-1.77zm0 5c1.61.94 4.19 1.77 7 1.77s5.39-.83 7-1.77V17c0 .66-3.13 2-7 2s-7-1.34-7-2v-1.77z"/></svg><span class="n">SQL / DB</span></div></div></a>
      <a href="#services" aria-label="PyTorch"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M12.783 2.016a.465.465 0 0 0-.616.14l-1.02 1.633a.466.466 0 0 0 .14.616l.24.15a6.002 6.002 0 0 1 2.923 5.485c-.09 3.033-2.482 5.498-5.516 5.56-3.324.067-6.03-2.614-6.03-5.938 0-2.585 1.637-4.79 3.937-5.61a.466.466 0 0 0 .285-.568l-.487-1.859a.466.466 0 0 0-.585-.328C2.518 4.39 0 7.747 0 11.662 0 16.82 4.18 21 9.338 21a9.34 9.34 0 0 0 9.34-9.338c0-3.924-2.42-7.29-5.895-8.648zM15.42 4.095a1.27 1.27 0 1 1-2.54 0 1.27 1.27 0 0 1 2.54 0z"/></svg><span class="n">PyTorch</span></div></div></a>
      <a href="#services" aria-label="Gemini AI"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 1 0 10 10A10.011 10.011 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8.01 8.01 0 0 1-8 8zm0-13a5 5 0 0 0-5 5 1 1 0 0 0 2 0 3 3 0 0 1 3-3 1 1 0 0 0 0-2zm0 6a1 1 0 1 0 1 1 1 1 0 0 0-1-1z"/></svg><span class="n">Gemini 2.5</span></div></div></a>
      <a href="#services" aria-label="OpenCV"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M12 2C9.24 2 7 4.24 7 7c0 .94.26 1.82.72 2.57L5.19 12.1A5.96 5.96 0 0 0 2 17c0 3.31 2.69 6 6 6 2.76 0 5.06-1.87 5.76-4.41l3.52.01c.7 2.54 3 4.4 5.72 4.4 3.31 0 6-2.69 6-6 0-2.07-1.06-3.89-2.67-4.96l-2.47-2.47C21.74 8.82 22 7.94 22 7c0-2.76-2.24-5-5-5-2.21 0-4.08 1.44-4.74 3.44A5.02 5.02 0 0 0 12 2zm0 3c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm-4 11c0-1.66 1.34-3 3-3s3 1.34 3 3-1.34 3-3 3-3-1.34-3-3zm9 0c0-1.66 1.34-3 3-3s3 1.34 3 3-1.34 3-3 3-3-1.34-3-3z"/></svg><span class="n">OpenCV</span></div></div></a>
      <a href="#services" aria-label="LangChain"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M16.5 3a4.5 4.5 0 0 0-3.8 2.08A4.5 4.5 0 0 0 7.5 3 4.5 4.5 0 0 0 3 7.5c0 1.94 1.23 3.6 2.97 4.22-.03.26-.05.52-.05.78 0 3.31 2.69 6 6 6s6-2.69 6-6c0-.26-.02-.52-.05-.78C19.77 11.1 21 9.44 21 7.5A4.5 4.5 0 0 0 16.5 3zm-9 6c-.83 0-1.5-.67-1.5-1.5S6.67 6 7.5 6s1.5.67 1.5 1.5S8.33 9 7.5 9zm9 0c-.83 0-1.5-.67-1.5-1.5S15.67 6 16.5 6s1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg><span class="n">LangChain</span></div></div></a>
      <a href="#services" aria-label="ChromaDB"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M4 4h16v4H4V4zm0 6h16v4H4v-4zm0 6h16v4H4v-4z"/></svg><span class="n">ChromaDB</span></div></div></a>
      <a href="#services" aria-label="FastAPI"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M12 2L3 7v10l9 5 9-5V7l-9-5zm0 2.2L18.8 8 12 11.8 5.2 8 12 4.2zM5 9.4l6 3.3v6.7l-6-3.3V9.4zm14 6.7l-6 3.3v-6.7l6-3.3v6.7z"/></svg><span class="n">FastAPI</span></div></div></a>
      <a href="#services" aria-label="Docker"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M13.983 11.078h2.119a.186.186 0 0 0 .186-.185V9.006a.186.186 0 0 0-.186-.186h-2.119a.185.185 0 0 0-.185.185v1.888c0 .102.083.185.185.185zm-2.954-5.43h2.118a.186.186 0 0 0 .186-.186V3.574a.186.186 0 0 0-.186-.185h-2.118a.185.185 0 0 0-.185.185v1.888c0 .102.082.185.185.185zm0 2.716h2.118a.187.187 0 0 0 .186-.186V6.29a.186.186 0 0 0-.186-.185h-2.118a.185.185 0 0 0-.185.185v1.887c0 .102.082.186.185.186zm-2.93 0h2.12a.186.186 0 0 0 .184-.186V6.29a.185.185 0 0 0-.185-.185H8.1a.185.185 0 0 0-.185.185v1.887c0 .102.083.186.185.186zm-2.964 0h2.119a.186.186 0 0 0 .185-.186V6.29a.185.185 0 0 0-.185-.185H5.136a.186.186 0 0 0-.186.185v1.887c0 .102.084.186.186.186zm5.893 2.714h2.119a.186.186 0 0 0 .186-.185V9.006a.185.185 0 0 0-.186-.186h-2.119a.185.185 0 0 0-.185.185v1.888c0 .102.082.185.185.185zm-2.929 0h2.119a.185.185 0 0 0 .185-.185V9.006a.185.185 0 0 0-.185-.186h-2.12a.186.186 0 0 0-.184.186v1.888c0 .102.083.185.185.185zm-2.964 0h2.119a.185.185 0 0 0 .185-.185V9.006a.185.185 0 0 0-.185-.186h-2.12a.186.186 0 0 0-.184.186v1.888c0 .102.083.185.185.185zm-2.928 0h2.119a.185.185 0 0 0 .185-.185V9.006a.185.185 0 0 0-.185-.186H2.208a.186.186 0 0 0-.186.186v1.888c0 .102.084.185.186.185zm21.724-.25c-.302-.198-.99-.344-1.744-.15-.367.095-.71.272-1.02.518-.328.261-.598.6-.795 1.002-.663 1.342-1.63 2.476-2.825 3.32-.977.69-2.106 1.15-3.303 1.345-1.127.185-2.28.163-3.4-.066-1.12-.228-2.18-.682-3.11-1.325a9.92 9.92 0 0 1-2.45-2.613c-.235-.37-.417-.768-.544-1.185l-.037-.123H.085c.074.832.32 1.637.72 2.373.91 1.67 2.27 3.03 3.91 3.92 1.77.96 3.78 1.44 5.8 1.4 2.29-.05 4.54-.7 6.47-1.87 1.83-1.11 3.3-2.68 4.24-4.55.26-.51.46-1.05.6-1.61.1-.38.16-.76.19-1.15.01-.15-.05-.27-.14-.33z"/></svg><span class="n">Docker</span></div></div></a>
      <a href="#services" aria-label="YOLOv8"><div class="cell with-dots"><div class="lines with-diagonal-lines"></div><div class="brand mono" data-ps><svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14.5v-9l6 4.5-6 4.5z"/></svg><span class="n">YOLOv8</span></div></div></a>
    </div>
  </section>'''
    html = re.sub(old_logos_pattern, new_logos_section, html, flags=re.DOTALL)

    # 6. Featured Projects Header
    html = html.replace(
        '<div class="framed"><i class="corner tl"></i><i class="corner tr"></i><i class="corner bl"></i><i class="corner br"></i><h2 class="f-h1" data-ps>Featured Projects</h2></div>',
        '<div class="framed"><i class="corner tl"></i><i class="corner tr"></i><i class="corner bl"></i><i class="corner br"></i><h2 class="f-h1" data-ps>Selected Systems &amp; Projects</h2></div>'
    )
    html = html.replace(
        '<p class="f-h4" data-ps>Eight selected builds from the last eighteen months — brand systems, product launches and a few experiments that got out of hand.</p>',
        '<p class="f-h4" data-ps>Production AI systems, low-latency streaming protocols, multi-agent evaluation frameworks, and high-performance automated pipelines.</p>'
    )

    # 7. Update the 8 Project Cards text & links (keeping the original images intact)
    # Card 1: Acuity Control
    html = html.replace('aria-label="Halide Launch"', 'aria-label="Acuity Control"')
    html = html.replace('<p class="cats" data-ps>Websites · Marketing · IRL</p>', '<p class="cats" data-ps>Systems · P2P Networking</p>')
    html = html.replace('<h3 class="f-h3" data-ps>Halide Launch</h3>', '<h3 class="f-h3" data-ps>Acuity Control</h3>')
    html = html.replace(
        '<p class="desc f-p" data-ps>Halide’s developer summit needed a home built for the moment: live schedules, speaker reveals and a ticket drop built for launch-day traffic.</p>',
        '<p class="desc f-p" data-ps>Ultra-low latency Mac display streaming and touch input capture over peer-to-peer WebSockets. Remote cursor, gestures, and displays without intermediary servers.</p>'
    )
    # Card 1: Acuity Control
    html = html.replace(
        '<p class="desc f-p" data-ps>Halide’s developer summit needed a home built for the moment: live schedules, speaker reveals and a ticket drop that held up on launch day.</p>',
        '<p class="desc f-p" data-ps>Low-latency remote control system for macOS from mobile devices. Real-time cursor navigation, media controls, keyboard input, and system shortcuts over local network socket streaming.</p>'
    )
    html = html.replace(
        '<a class="go f-p" href="#work" data-ps><span>View project</span>',
        '<a class="go f-p" href="https://github.com/shashanthnetha/Acuity-control-mac-through-mobile-" target="_blank" rel="noopener" data-ps><span>View Repository</span>',
        1
    )

    # Card 2: AgriSense AI
    html = html.replace('aria-label="Northwind Labs"', 'aria-label="AgriSense AI"')
    html = html.replace('<p class="cats" data-ps>Brand System · Photography</p>', '<p class="cats" data-ps>Multimodal AI · RAG Architecture</p>')
    html = html.replace('<h3 class="f-h3" data-ps>Northwind Labs</h3>', '<h3 class="f-h3" data-ps>AgriSense AI</h3>')
    html = html.replace(
        '<p class="desc f-p" data-ps>An energy company that had outgrown its logo. We rebuilt the identity around the people who climb the towers.</p>',
        '<p class="desc f-p" data-ps>Multi-agent crop disease diagnosis platform combining Gemini 2.0 Flash Vision for leaf pathogen identification, ChromaDB vector search across 50+ conditions, and multilingual voice advisory.</p>'
    )
    html = html.replace(
        '<a class="go f-p" href="#work" data-ps><span>View project</span>',
        '<a class="go f-p" href="https://github.com/shashanthnetha/agrisense-ai" target="_blank" rel="noopener" data-ps><span>View Repository</span>',
        1
    )

    # Card 3: courtroom-env
    html = html.replace('aria-label="Lumenary"', 'aria-label="courtroom-env"')
    html = html.replace('<p class="cats" data-ps>Websites · Product Launch</p>', '<p class="cats" data-ps>Multi-Agent Benchmark · Legal AI</p>')
    html = html.replace('<h3 class="f-h3" data-ps>Lumenary</h3>', '<h3 class="f-h3" data-ps>courtroom-env</h3>')
    html = html.replace(
        '<p class="desc f-p" data-ps>A quiet product deserved a loud launch. The story-driven site sold through the first hardware run in a weekend.</p>',
        '<p class="desc f-p" data-ps>Adversarial multi-agent legal benchmark simulating trial arguments, cross-examinations, and judicial deliberation with structured consensus evaluation.</p>'
    )
    html = html.replace(
        '<a class="go f-p" href="#work" data-ps><span>View project</span>',
        '<a class="go f-p" href="https://github.com/shashanthnetha/courtroom-env" target="_blank" rel="noopener" data-ps><span>View Repository</span>',
        1
    )

    # Card 4: IntelliCredit
    html = html.replace('aria-label="Quillworks"', 'aria-label="IntelliCredit"')
    html = html.replace('<p class="cats" data-ps>Identity · Print</p>', '<p class="cats" data-ps>Machine Learning · Financial AI</p>')
    html = html.replace('<h3 class="f-h3" data-ps>Quillworks</h3>', '<h3 class="f-h3" data-ps>IntelliCredit</h3>')
    html = html.replace(
        '<p class="desc f-p" data-ps>A stationery house with a hundred-year archive and no way to show it. We gave the catalogue a spine again.</p>',
        '<p class="desc f-p" data-ps>Automated corporate credit risk appraisal engine integrating Gemini Vision statement extraction with Random Forest default scoring and SHAP explainability analysis.</p>'
    )
    html = html.replace(
        '<a class="go f-p" href="#work" data-ps><span>View project</span>',
        '<a class="go f-p" href="https://github.com/shashanthnetha" target="_blank" rel="noopener" data-ps><span>View Repository</span>',
        1
    )

    # Card 5: NetWorth App
    html = html.replace('aria-label="Kestrel Studios"', 'aria-label="NetWorth App"')
    html = html.replace('<p class="cats" data-ps>Websites · Editorial</p>', '<p class="cats" data-ps>Full-Stack · Personal Finance</p>')
    html = html.replace('<h3 class="f-h3" data-ps>Kestrel Studios</h3>', '<h3 class="f-h3" data-ps>NetWorth App</h3>')
    html = html.replace(
        '<p class="desc f-p" data-ps>We fused fashion drops with interactive storytelling, turning a seasonal lookbook into a world people shared.</p>',
        '<p class="desc f-p" data-ps>Cross-platform personal wealth simulator and asset projection engine engineered with Next.js, Zustand state management, and real-time portfolio milestone tracking.</p>'
    )
    html = html.replace(
        '<a class="go f-p" href="#work" data-ps><span>View project</span>',
        '<a class="go f-p" href="https://github.com/shashanthnetha/NetWorth_app" target="_blank" rel="noopener" data-ps><span>View Repository</span>',
        1
    )

    # Card 6: Analytics Shorts Engine
    html = html.replace('aria-label="Cobaltine"', 'aria-label="Analytics Shorts Engine"')
    html = html.replace('<p class="cats" data-ps>Space Design · Wayfinding</p>', '<p class="cats" data-ps>Automation · Media Pipeline</p>')
    html = html.replace('<h3 class="f-h3" data-ps>Cobaltine</h3>', '<h3 class="f-h3" data-ps>Analytics Shorts</h3>')
    html = html.replace(
        '<p class="desc f-p" data-ps>Six floors, one colour and a lighting rule that does the wayfinding so the signage does not have to.</p>',
        '<p class="desc f-p" data-ps>Autonomous short-form video generation pipeline utilizing MoviePy, Whisper transcription, and algorithmic visual pacing for automated technical summaries.</p>'
    )
    html = html.replace(
        '<a class="go f-p" href="#work" data-ps><span>View project</span>',
        '<a class="go f-p" href="https://github.com/shashanthnetha/analytics_shorts" target="_blank" rel="noopener" data-ps><span>View Repository</span>',
        1
    )

    # Card 7: NutriLens
    html = html.replace('aria-label="Shop Moonrake"', 'aria-label="NutriLens"')
    html = html.replace('<p class="cats" data-ps>Commerce · Campaign</p>', '<p class="cats" data-ps>Android · Mobile Edge AI</p>')
    html = html.replace('<h3 class="f-h3" data-ps>Shop Moonrake</h3>', '<h3 class="f-h3" data-ps>NutriLens</h3>')
    html = html.replace(
        '<p class="desc f-p" data-ps>A creator with millions of viewers needed a storefront that felt like the videos: fast, loud, impossible to scroll past.</p>',
        '<p class="desc f-p" data-ps>On-device food safety and ingredient inspection application built with Kotlin, CameraX, and ML Kit optical character recognition for real-time allergen detection.</p>'
    )
    html = html.replace(
        '<a class="go f-p" href="#work" data-ps><span>View project</span>',
        '<a class="go f-p" href="https://github.com/shashanthnetha" target="_blank" rel="noopener" data-ps><span>View Repository</span>',
        1
    )

    # Card 8: Radius Mesh
    html = html.replace('aria-label="Signalhaus"', 'aria-label="Radius Mesh"')
    html = html.replace('<p class="cats" data-ps>Product · Interface</p>', '<p class="cats" data-ps>Decentralized · P2P Protocol</p>')
    html = html.replace('<h3 class="f-h3" data-ps>Signalhaus</h3>', '<h3 class="f-h3" data-ps>Radius Mesh</h3>')
    html = html.replace(
        '<p class="desc f-p" data-ps>A desktop radio with one knob and no screen. Most of the work was deciding what to leave out.</p>',
        '<p class="desc f-p" data-ps>Off-grid localized mesh messaging infrastructure utilizing WiFi Direct and Bluetooth Low Energy for decentralized communication during cellular network outages.</p>'
    )
    html = html.replace(
        '<a class="go f-p" href="#work" data-ps><span>View project</span>',
        '<a class="go f-p" href="https://github.com/shashanthnetha" target="_blank" rel="noopener" data-ps><span>View Repository</span>',
        1
    )

    # 8. Capabilities Section
    html = html.replace(
        '<p data-ps>We\'re here to make the extraordinary.</p>\n      <p data-ps>No shortcuts — just bold, precise work that raises the bar &amp; leaves a mark.</p>',
        '<p data-ps>Engineering robust intelligence from model weights to live runtime.</p>\n      <p data-ps>No shortcuts — just battle-tested code, deterministic pipelines &amp; low latency.</p>'
    )
    html = html.replace(
        '<h3 class="f-h4" data-ps><a class="actionable" href="#showcase">Websites &amp; Features</a></h3>\n          <p class="f-h4" data-ps>From pre-launch teasers to full redesigns, we design and engineer sites that earn attention and turn it into action.</p>\n          <div class="tags f-p"><span>Product Strategy</span><span>UX/UI Design</span><span>Engineering</span><span>3D &amp; Motion</span></div>',
        '<h3 class="f-h4" data-ps><a class="actionable" href="#work">AI &amp; Agentic Systems</a></h3>\n          <p class="f-h4" data-ps>Multimodal vision inference, structured function calling, LangChain orchestrations, and high-precision RAG architectures with ChromaDB.</p>\n          <div class="tags f-p"><span>Gemini 2.5</span><span>PyTorch</span><span>ChromaDB</span><span>LangChain</span><span>OpenCV</span><span>YOLOv8</span></div>'
    )
    html = html.replace(
        '<h3 class="f-h4" data-ps><a class="actionable" href="#showcase">Visual Branding</a></h3>\n          <p class="f-h4" data-ps>From lean identities for new companies to full brand platforms for category leaders, we build systems that scale without going stale.</p>\n          <div class="tags f-p"><span>Visual Identity</span><span>Brand Systems</span></div>',
        '<h3 class="f-h4" data-ps><a class="actionable" href="#work">Core Engineering &amp; Fundamentals</a></h3>\n          <p class="f-h4" data-ps>High-performance asynchronous programming, data structures, algorithm optimization, and native hardware utilization.</p>\n          <div class="tags f-p"><span>Python</span><span>Java</span><span>C</span><span>SQL</span><span>Concurrency</span></div>'
    )
    html = html.replace(
        '<h3 class="f-h4" data-ps><a class="actionable" href="#showcase">IRL Experience Design</a></h3>\n          <p class="f-h4" data-ps>From annual summits to weekend pop-ups, we design in-person moments people remember long after the doors close.</p>\n          <div class="tags f-p"><span>Visual Identity</span><span>Space Design</span><span>Keynote Design</span><span>Digital &amp; Interactive</span></div>',
        '<h3 class="f-h4" data-ps><a class="actionable" href="#work">Backend &amp; API Architecture</a></h3>\n          <p class="f-h4" data-ps>Production-ready REST APIs, real-time WebSocket communication, relational data modeling, and containerized deployment.</p>\n          <div class="tags f-p"><span>FastAPI</span><span>Docker</span><span>PostgreSQL</span><span>WebSockets</span><span>Redis</span></div>'
    )
    html = html.replace(
        '<h3 class="f-h4" data-ps><a class="actionable" href="#showcase">Marketing Execution</a></h3>\n          <p class="f-h4" data-ps>From brand to product marketing, we plug into marketing teams to ship the assets that drive awareness, demand and conversion.</p>\n          <div class="tags f-p"><span>Campaign Content</span><span>Growth Experiments</span><span>Sales Materials</span></div>',
        '<h3 class="f-h4" data-ps><a class="actionable" href="#work">Interactive &amp; Client Applications</a></h3>\n          <p class="f-h4" data-ps>Modern web frontend interfaces, client-side state management, and native Android application development.</p>\n          <div class="tags f-p"><span>Next.js</span><span>TypeScript</span><span>Zustand</span><span>Android Kotlin</span><span>CameraX</span></div>'
    )

    # 9. Contact Section (Eliminates hello@sublevel.studio)
    html = html.replace(
        '<p class="lead f-h1" data-ps>Let\'s build something loud.</p>\n      <div class="mail f-h1" data-ps><a href="mailto:hello@sublevel.studio"><span class="actionable">hello@sublevel.studio</span></a></div>',
        '<p class="lead f-h1" data-ps>Let\'s build intelligent systems together.</p>\n      <div class="mail f-h1" data-ps><a href="mailto:shashanthnetha@gmail.com"><span class="actionable">shashanthnetha@gmail.com</span></a></div>'
    )

    # 10. Remove Newsletter Section ("Stay plugged into the build log...") as requested
    old_fcard_pattern = r'\s*<div class="grid-layout fcard-wrap">.*?</div>\s*</div>'
    html = re.sub(old_fcard_pattern, '', html, flags=re.DOTALL)

    # 11. Footer Mark & Links (Eliminates SUBLEVEL.26 and © sublevel.studio LLC 2026)
    html = html.replace(
        '<svg viewBox="0 0 1673 149" xmlns="http://www.w3.org/2000/svg" aria-label="SUBLEVEL.26"><text x="0" y="140" textLength="1673" lengthAdjust="spacingAndGlyphs" font-family="Geist, \'Geist Fallback\', Arial, sans-serif" font-weight="500" font-size="196" letter-spacing="-6">SUBLEVEL.26</text></svg>',
        '<svg viewBox="0 0 1673 149" xmlns="http://www.w3.org/2000/svg" aria-label="SHASHANTH.26"><text x="0" y="140" textLength="1673" lengthAdjust="spacingAndGlyphs" font-family="Geist, \'Geist Fallback\', Arial, sans-serif" font-weight="500" font-size="196" letter-spacing="-6">SHASHANTH.26</text></svg>'
    )
    html = html.replace(
        '<div class="links f-h3"><a class="blink" href="#top">Home</a><a class="blink" href="#services">Services</a><a class="blink" href="#showcase">Showcase</a><a class="blink" href="#people">People</a><a class="blink" href="#blog">Blog</a><a class="blink" href="#lab">Lab</a><a class="blink" href="mailto:hello@sublevel.studio">Contact Us</a></div>',
        '<div class="links f-h3"><a class="blink" href="#top">Home</a><a class="blink" href="#showcase">Arsenal</a><a class="blink" href="#work">Projects</a><a class="blink" href="https://github.com/shashanthnetha" target="_blank" rel="noopener">GitHub</a><a class="blink" href="https://linkedin.com/in/shashanth-pittala" target="_blank" rel="noopener">LinkedIn</a><a class="blink" href="mailto:shashanthnetha@gmail.com">Contact</a></div>'
    )
    html = html.replace(
        '<div class="social"><a href="#lab" aria-label="X" title="X"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3.2 2.6h4.1l3.8 5.1 4.3-5.1h2.4l-5.6 6.6 6 8.2h-4.1l-4-5.4-4.6 5.4H3.1l6-7.1-5.9-7.7Zm2.3 1.5 8.5 11.4h1.6L7.1 4.1H5.5Z"/></svg></a><a href="#lab" aria-label="Instagram" title="Instagram"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M6.6 2.5h6.8a4.1 4.1 0 0 1 4.1 4.1v6.8a4.1 4.1 0 0 1-4.1 4.1H6.6a4.1 4.1 0 0 1-4.1-4.1V6.6a4.1 4.1 0 0 1 4.1-4.1Zm0 1.6A2.5 2.5 0 0 0 4.1 6.6v6.8a2.5 2.5 0 0 0 2.5 2.5h6.8a2.5 2.5 0 0 0 2.5-2.5V6.6a2.5 2.5 0 0 0-2.5-2.5H6.6Zm3.4 2.6a3.3 3.3 0 1 1 0 6.6 3.3 3.3 0 0 1 0-6.6Zm0 1.6a1.7 1.7 0 1 0 0 3.4 1.7 1.7 0 0 0 0-3.4Zm3.9-2.5a.95.95 0 1 1 0 1.9.95.95 0 0 1 0-1.9Z"/></svg></a><a href="#lab" aria-label="GitHub" title="GitHub"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 2.2a7.8 7.8 0 0 0-2.5 15.2c.4.07.54-.17.54-.38v-1.5c-2.2.44-2.66-.94-2.66-.94-.36-.92-.88-1.16-.88-1.16-.72-.5.05-.48.05-.48.8.06 1.22.82 1.22.82.7 1.22 1.86.87 2.32.66.07-.52.28-.87.5-1.07-1.75-.2-3.6-.88-3.6-3.92 0-.87.31-1.58.82-2.13-.08-.2-.36-1.01.08-2.11 0 0 .67-.21 2.2.81a7.6 7.6 0 0 1 4 0c1.53-1.02 2.2-.81 2.2-.81.44 1.1.16 1.91.08 2.11.51.55.82 1.26.82 2.13 0 3.05-1.86 3.72-3.63 3.91.29.25.54.73.54 1.47v2.18c0 .21.14.46.55.38A7.8 7.8 0 0 0 10 2.2Z"/></svg></a><a href="#lab" aria-label="LinkedIn" title="LinkedIn"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4.3 2.6a1.75 1.75 0 1 1 0 3.5 1.75 1.75 0 0 1 0-3.5ZM2.8 7.5h3v9.9h-3V7.5Zm5.1 0h2.87v1.36h.04c.4-.73 1.38-1.5 2.83-1.5 3.03 0 3.59 1.9 3.59 4.38v5.66h-3v-5.02c0-1.2-.02-2.74-1.7-2.74-1.7 0-1.96 1.3-1.96 2.65v5.11h-3V7.5Z"/></svg></a></div>',
        '<div class="social"><a href="https://github.com/shashanthnetha" target="_blank" rel="noopener" aria-label="GitHub" title="GitHub"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 2.2a7.8 7.8 0 0 0-2.5 15.2c.4.07.54-.17.54-.38v-1.5c-2.2.44-2.66-.94-2.66-.94-.36-.92-.88-1.16-.88-1.16-.72-.5.05-.48.05-.48.8.06 1.22.82 1.22.82.7 1.22 1.86.87 2.32.66.07-.52.28-.87.5-1.07-1.75-.2-3.6-.88-3.6-3.92 0-.87.31-1.58.82-2.13-.08-.2-.36-1.01.08-2.11 0 0 .67-.21 2.2.81a7.6 7.6 0 0 1 4 0c1.53-1.02 2.2-.81 2.2-.81.44 1.1.16 1.91.08 2.11.51.55.82 1.26.82 2.13 0 3.05-1.86 3.72-3.63 3.91.29.25.54.73.54 1.47v2.18c0 .21.14.46.55.38A7.8 7.8 0 0 0 10 2.2Z"/></svg></a><a href="https://linkedin.com/in/shashanth-pittala" target="_blank" rel="noopener" aria-label="LinkedIn" title="LinkedIn"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4.3 2.6a1.75 1.75 0 1 1 0 3.5 1.75 1.75 0 0 1 0-3.5ZM2.8 7.5h3v9.9h-3V7.5Zm5.1 0h2.87v1.36h.04c.4-.73 1.38-1.5 2.83-1.5 3.03 0 3.59 1.9 3.59 4.38v5.66h-3v-5.02c0-1.2-.02-2.74-1.7-2.74-1.7 0-1.96 1.3-1.96 2.65v5.11h-3V7.5Z"/></svg></a><a href="mailto:shashanthnetha@gmail.com" aria-label="Email" title="Email: shashanthnetha@gmail.com"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 4h14a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1zm0 2v.5l7 4.5 7-4.5V6H3zm14 8V8.2l-6.47 4.16a1 1 0 0 1-1.06 0L3 8.2V14h14z"/></svg></a></div>'
    )
    html = html.replace(
        '<p class="copy f-p">© sublevel.studio LLC 2026 all rights reserved</p>',
        '<p class="copy f-p">© 2026 Shashanth Pittala. All rights reserved.</p>'
    )

    # 12. Raw Machine Index (#machine pre.sr-only)
    old_pre_pattern = r'<pre class="sr-only">.*?</pre>'
    new_pre_content = '''<pre class="sr-only"> █████ █   █  ███   ████ █   █  ███  █   █ █████ █   █ 
 █     █   █ █   █ █     █   █ █   █ ██  █   █   █   █ 
 █████ █████ █████  ███  █████ █████ █ █ █   █   █████ 
     █ █   █ █   █     █ █   █ █   █ █  ██   █   █   █ 
 █████ █   █ █   █ ████  █   █ █   █ █   █   █   █   █ 

SHASHANTH PITTALA :: MACHINE-READABLE PROFILE

# PLAIN-TEXT MIRROR FOR AI AGENTS, RECRUITERS, AND HUMANS WHO PREFER IT RAW.

── ABOUT ─────────────────────────────────────────────────────────
NAME .......... SHASHANTH PITTALA (SHA)
ROLE .......... AI & SYSTEMS ENGINEER
LOCATION ...... HYDERABAD, TELANGANA, INDIA
EDUCATION ..... B.TECH CSE (AI & ML) @ CMRCET · NXTWAVE FELLOW
GITHUB ........ github.com/shashanthnetha (46 REPOSITORIES)
LINKEDIN ...... linkedin.com/in/shashanth-pittala
EMAIL ......... shashanthnetha@gmail.com

── CORE ARSENAL ──────────────────────────────────────────────────
LANGUAGES ..... PYTHON, JAVA, C, SQL, TYPESCRIPT
AI / ML ....... GEMINI 2.5 VISION, PYTORCH (APPLE MPS), OPENCV,
                LANGCHAIN, CHROMADB / PINECONE (RAG), YOLOV8
SYSTEMS ....... FASTAPI, REST APIS, DOCKER, POSTGRESQL, REDIS
MOBILE ........ NATIVE ANDROID (KOTLIN, JETPACK COMPOSE, CAMERAX)

── FEATURED BUILDS ───────────────────────────────────────────────
[01] ACUITY CONTROL ........ Ultra-low Latency Mac Display & Touch over P2P
[02] AGRISENSE AI .......... Crop Disease Detection & Multilingual Advisory
[03] COURTROOM-ENV ......... Legal Multi-Agent Benchmark (0.9667 Accuracy)
[04] INTELLICREDIT ......... AI Credit Appraisal with Gemini Vision & SHAP
[05] NETWORTH .............. Financial Simulator (Next.js, Zustand, Capacitor)
[06] ANALYTICS_SHORTS ...... Programmatic Video Engine on Apple Silicon M3
[07] NUTRILENS ............. Android Food Safety Scanner (CameraX + ML Kit)
[08] RADIUS ................ Offline P2P Mesh Chat (WiFi Direct + Bluetooth)

STATUS: AVAILABLE FOR PRODUCTION AI ROLES AND HIGH-IMPACT BUILDS.</pre>'''
    html = re.sub(old_pre_pattern, new_pre_content, html, flags=re.DOTALL)

    # 13. Three.js 3D Arcade Room & Canvas Textures
    # Neon sign on back wall
    html = html.replace("strokeText('sublevel.', w / 2, h / 2 + 8)", "strokeText('shashanth.', w / 2, h / 2 + 8)")
    html = html.replace("fillText('sublevel.', w / 2, h / 2 + 8)", "fillText('shashanth.', w / 2, h / 2 + 8)")

    # Cabinet marquee header
    html = html.replace("fillText('SUBLEVEL', w / 2, h / 2 + 6)", "fillText('SHASHANTH', w / 2, h / 2 + 6)")

    # Basketball backboard
    html = html.replace("strokeText('SBLVL', 412, 232)", "strokeText('SHA', 412, 232)")
    html = html.replace("fillText('SBLVL', 412, 232)", "fillText('SHA', 412, 232)")

    # Ticker ribbon
    html = html.replace(
        "g.fillText('SUBLEVEL   ///   WE BUILD THE STUFF PEOPLE REMEMBER   ///   OPEN LATE   ///   NOW PLAYING: SUBLEVEL DEFENDER   ///   ', 0, 34);",
        "g.fillText('SHASHANTH PITTALA   ///   AI & SYSTEMS ENGINEER   ///   ALWAYS BUILDING   ///   NOW PLAYING: SHA DEFENDER   ///   HYDERABAD, INDIA   ///   ', 0, 34);"
    )

    # Cabinet side art
    html = html.replace("g.fillText('SUBLEVEL', 0, 0);", "g.fillText('SHASHANTH', 0, 0);")

    # Cabinet CRT bezel
    html = html.replace("g.fillText('SUBLEVEL DEFENDER', w / 2, 40);", "g.fillText('SHA DEFENDER', w / 2, 40);")

    # Cabinet panel
    html = html.replace("g.fillText('SUBLEVEL', 370, 28);", "g.fillText('SHASHANTH', 370, 28);")

    # Vertical banner
    html = html.replace("fillText('SUBLEVEL', 0, 0)", "fillText('SHASHANTH', 0, 0)")

    # 3D Arcade game CRT canvas
    html = html.replace("g.fillText('SUBLEVEL', cx, 110); g.fillText('DEFENDER', cx, 166);", "g.fillText('SHA', cx, 110); g.fillText('DEFENDER', cx, 166);")
    html = html.replace("g.fillText('SUBLEVEL', cx, 118); g.fillText('DEFENDER', cx, 166);", "g.fillText('SHA', cx, 118); g.fillText('DEFENDER', cx, 166);")
    html = html.replace("g.fillText('SUBLEVEL DEFENDER', 256, 130);", "g.fillText('SHA DEFENDER', 256, 130);")

    # Update 3D TV Screen slides in PORTFOLIO
    html = html.replace(
        "{ title: 'Halide Launch', kind: 'Website · Event', desc: 'Real-time summit site with live schedule and ticket drop.', draw(g, w, h, t) {",
        "{ title: 'Acuity Control', kind: 'Systems · P2P Remote', desc: 'Ultra-low latency Mac display & touch streaming over WebSockets.', draw(g, w, h, t) {"
    )
    html = html.replace("g.fillText('LAUNCH', 22, 62); g.fillText(\"2026\", 22, 134);", "g.fillText('ACUITY', 22, 62); g.fillText('CONTROL', 22, 134);")

    html = html.replace(
        "{ title: 'Lumenary', kind: 'Website · Product launch', desc: 'Story-driven launch site for a first hardware release.', draw(g, w, h, t) {",
        "{ title: 'courtroom-env', kind: 'Multi-Agent · Benchmark', desc: 'Adversarial courtroom simulation benchmark achieving 0.9667 accuracy.', draw(g, w, h, t) {"
    )
    html = html.replace("g.fillText('Daylight,', 350, 130); g.fillText('captured.', 350, 180);", "g.fillText('Legal AI,', 350, 130); g.fillText('benchmarked.', 350, 180);")

    html = html.replace(
        "{ title: 'Kestrel Studios', kind: 'Website · Lookbook', desc: 'A seasonal lookbook turned into a browsable world.', draw(g, w, h, t) {",
        "{ title: 'NetWorth App', kind: 'Full-Stack · Simulation', desc: 'Cross-platform wealth simulator and projection engine.', draw(g, w, h, t) {"
    )
    html = html.replace("g.fillText('SS26 LOOKBOOK — SCROLL TO EXPLORE', 40, 48);", "g.fillText('NETWORTH APP — ASSET SIMULATOR', 40, 48);")

    html = html.replace(
        "{ title: 'Shop Moonrake', kind: 'Storefront', desc: 'A creator storefront that feels like the videos.', draw(g, w, h, t) {",
        "{ title: 'Analytics Shorts', kind: 'Automation · Video AI', desc: 'Autonomous short-form video engine on Apple Silicon M3.', draw(g, w, h, t) {"
    )
    html = html.replace("g.fillText('MOONRAKE', w / 2, 80);", "g.fillText('SHORTS AI', w / 2, 80);")

    html = html.replace(
        "{ title: 'Northwind Labs', kind: 'Product UI · Dashboard', desc: 'Operations console for a logistics platform.', draw(g, w, h, t) {",
        "{ title: 'AgriSense AI', kind: 'Multimodal AI · RAG', desc: 'Multi-agent crop disease diagnosis with Gemini Vision & ChromaDB.', draw(g, w, h, t) {"
    )
    html = html.replace("g.fillText('Northwind Fleet Ops', 170, 40);", "g.fillText('AgriSense AI Diagnosis', 170, 40);")

    html = html.replace(
        "{ title: 'Sublevel Defender', kind: 'Lab · Game', desc: 'The lobby arcade game. Click the cabinet to play.'",
        "{ title: 'Sha Defender', kind: 'Lab · Retro Game', desc: 'The lobby arcade game. Click the cabinet to play.'"
    )
    html = html.replace("g.fillText('SUBLEVEL DEFENDER', cx, 80);", "g.fillText('SHA DEFENDER', cx, 80);")

    html = html.replace(
        "{ title: 'Cobaltine', kind: 'Brand identity', desc: 'Visual identity and motion system for a data company.', draw(g, w, h, t) {",
        "{ title: 'IntelliCredit', kind: 'Machine Learning · AI', desc: 'Automated credit appraisal with Gemini Vision & SHAP.', draw(g, w, h, t) {"
    )
    html = html.replace("g.fillText('Cobaltine', 420, 190);", "g.fillText('IntelliCredit', 420, 190);")
    html = html.replace("g.fillText('COBALTINE — IDENTITY 2026 —', i * 400 - off, 430);", "g.fillText('INTELLICREDIT — AI CREDIT 2026 —', i * 400 - off, 430);")

    # 14. Comment line mentioning sublevel
    html = html.replace(
        "painters and renderer logic are the authored code. The terminal LOG is injectable so the sublevel",
        "painters and renderer logic are the authored code. The terminal LOG is injectable so the shashanth"
    )

    # 15. Slash key shortcut
    html = html.replace(
        "location.href = 'mailto:hello@sublevel.studio';",
        "location.href = 'mailto:shashanthnetha@gmail.com';"
    )

    # 16. Replace exact single line of SUBLEVEL_LOG without touching any other line!
    # In sublevel-studio.html, line 4985 starts with "  const SUBLEVEL_LOG = [["
    # Let's do line-by-line check:
    lines = html.splitlines(keepends=True)
    replaced_log = False
    for i, l in enumerate(lines):
        if l.strip().startswith('const SUBLEVEL_LOG = [['):
            new_log_json = '''  const SHASHANTH_LOG = [
  [" █████ █   █  ███   ████ █   █  ███  █   █ █████ █   █ ", "p"],
  [" █     █   █ █   █ █     █   █ █   █ ██  █   █   █   █ ", "p"],
  [" █████ █████ █████  ███  █████ █████ █ █ █   █   █████ ", "p"],
  ["     █ █   █ █   █     █ █   █ █   █ █  ██   █   █   █ ", "p"],
  [" █████ █   █ █   █ ████  █   █ █   █ █   █   █   █   █ ", "p"],
  ["", "p"],
  ["/AI/HOME  /AI/PROJECTS  /AI/ARSENAL  /AI/GITHUB  /AI/LINKEDIN  /AI/CONTACT", "a"],
  ["", "p"],
  ["SHASHANTH PITTALA :: MACHINE-READABLE PROFILE", "p"],
  ["", "p"],
  ["# PLAIN-TEXT MIRROR FOR AI AGENTS, RECRUITERS, AND HUMANS WHO PREFER IT RAW.", "d"],
  ["", "p"],
  ["── ABOUT ─────────────────────────────────────────────────────────", "d"],
  ["NAME .......... SHASHANTH PITTALA (SHA)", "p"],
  ["ROLE .......... AI & SYSTEMS ENGINEER", "p"],
  ["LOCATION ...... HYDERABAD, TELANGANA, INDIA", "p"],
  ["EDUCATION ..... B.TECH CSE (AI & ML) @ CMRCET · NXTWAVE FELLOW", "p"],
  ["GITHUB ........ github.com/shashanthnetha (46 REPOSITORIES)", "p"],
  ["LINKEDIN ...... linkedin.com/in/shashanth-pittala", "p"],
  ["EMAIL ......... shashanthnetha@gmail.com", "p"],
  ["", "p"],
  ["── CORE ARSENAL ──────────────────────────────────────────────────", "d"],
  ["LANGUAGES ..... PYTHON, JAVA, C, SQL, TYPESCRIPT", "p"],
  ["AI / ML ....... GEMINI 2.5 VISION, PYTORCH (APPLE MPS), OPENCV,", "p"],
  ["               LANGCHAIN, CHROMADB / PINECONE (RAG), YOLOV8", "p"],
  ["SYSTEMS ....... FASTAPI, REST APIS, DOCKER, POSTGRESQL, REDIS", "p"],
  ["MOBILE ........ NATIVE ANDROID (KOTLIN, JETPACK COMPOSE, CAMERAX)", "p"],
  ["", "p"],
  ["── FEATURED BUILDS ───────────────────────────────────────────────", "d"],
  ["[01] ACUITY CONTROL ........ Ultra-low Latency Mac Display & Touch over P2P", "p"],
  ["[02] AGRISENSE AI .......... Crop Disease Detection & Multilingual Advisory", "p"],
  ["[03] COURTROOM-ENV ......... Legal Multi-Agent Benchmark (0.9667 Accuracy)", "p"],
  ["[04] INTELLICREDIT ......... AI Credit Appraisal with Gemini Vision & SHAP", "p"],
  ["[05] NETWORTH .............. Financial Simulator (Next.js, Zustand, Capacitor)", "p"],
  ["[06] ANALYTICS_SHORTS ...... Programmatic Video Engine on Apple Silicon M3", "p"],
  ["[07] NUTRILENS ............. Android Food Safety Scanner (CameraX + ML Kit)", "p"],
  ["[08] RADIUS ................ Offline P2P Mesh Chat (WiFi Direct + Bluetooth)", "p"],
  ["", "p"],
  ["STATUS: AVAILABLE FOR PRODUCTION AI ROLES AND HIGH-IMPACT BUILDS.", "a"]
];\n'''
            lines[i] = new_log_json
            replaced_log = True
            print(f"Replaced SUBLEVEL_LOG at line {i+1}")
            break

    assert replaced_log, "Failed to locate and replace SUBLEVEL_LOG line"
    html = "".join(lines)

    # Replace variable reference in crt mount
    html = html.replace('}, SUBLEVEL_LOG);', '}, SHASHANTH_LOG);')

    # 17. High-FPS Performance Optimizations
    # A. Three.js DPR Cap on high-DPI displays (1.25x instead of 1.5x / 2.0x)
    html = html.replace('let DPR = Math.min(window.devicePixelRatio || 1, 1.5);', 'let DPR = Math.min(window.devicePixelRatio || 1, 1.25);')

    # B. Eliminate resize() from 60fps render() loop (prevent layout thrashing)
    html = html.replace('function render(now) {\n  resize();', 'function render(now) {')

    # C. Throttle TV static and textures in home view (reduces 70% of CPU-to-GPU texture uploads)
    old_tv_loop = """  if (frame % 2 === 0) { drawStatic(staticTexA, t, false); drawStatic(staticTexB, t, true); for (const tx of tvTextures) tx.needsUpdate = true; }
  TV.forEach((tv, i) => {
    const focused = state.mode === 'tv' && state.tvIndex === i;
    if (focused || (frame + i) % 6 === 0) { tv.site.draw(tv.ctx, 640, 480, t); tv.tex.needsUpdate = true; }
    const target = state.mode === 'tv' ? (focused ? 0.05 : 0.45) : 0.7;
    tv.snowLevel += (target - tv.snowLevel) * 0.08; tv.snow.material.opacity = tv.snowLevel; tv.light.intensity = 0.7 + (1 - tv.snowLevel) * 0.8;
  });"""
    new_tv_loop = """  const isTvMode = state.mode === 'tv';
  if (frame % 4 === 0 && (isTvMode || frame % 8 === 0)) {
    drawStatic(staticTexA, t, false); drawStatic(staticTexB, t, true);
    for (const tx of tvTextures) tx.needsUpdate = true;
  }
  TV.forEach((tv, i) => {
    const focused = isTvMode && state.tvIndex === i;
    const shouldDraw = focused ? true : (isTvMode ? (frame + i) % 6 === 0 : (frame + i * 3) % 18 === 0);
    if (shouldDraw) { tv.site.draw(tv.ctx, 640, 480, t); tv.tex.needsUpdate = true; }
    const target = isTvMode ? (focused ? 0.05 : 0.45) : 0.7;
    tv.snowLevel += (target - tv.snowLevel) * 0.08; tv.snow.material.opacity = tv.snowLevel; tv.light.intensity = 0.7 + (1 - tv.snowLevel) * 0.8;
  });"""
    html = html.replace(old_tv_loop, new_tv_loop)

    # D. VHS overlay resolution & scroll pausing (75% GPU fill rate reduction)
    old_vhs_frame = """    function frame(now) {
      const dpr = Math.min(devicePixelRatio || 1, 2); const w = Math.round(innerWidth * dpr), h = Math.round(innerHeight * dpr);
      if (cv.width !== w || cv.height !== h) { cv.width = w; cv.height = h; }"""
    new_vhs_frame = """    function frame(now) {
      const dpr = 1.0; const w = Math.round(innerWidth * dpr), h = Math.round(innerHeight * dpr);
      if (cv.width !== w || cv.height !== h) { cv.width = w; cv.height = h; }
      if (window.scrollY > (innerHeight * 1.5) && !document.body.classList.contains('machine')) {
        requestAnimationFrame(frame);
        return;
      }"""
    html = html.replace(old_vhs_frame, new_vhs_frame)

    # E. ParticleScroll responsive tuning (snappy, zero sticky drag)
    old_ps_call = "window.ParticleScroll.mountParticleScroll('[data-ps]', { point: 0.68, band: 330, density: 2, size: 1.25, spread: 200, gravity: 0.35, drift: 0.9, swirl: 70, stagger: 0.55, fade: 0.42, settle: 0.7, hold: 1.15, smoothing: 0.26, tintA: [1.0, 0.3, 0.0], tintB: [1.0, 0.82, 0.2] });"
    new_ps_call = "window.ParticleScroll.mountParticleScroll('[data-ps]', { point: 0.68, band: 280, density: 1.4, size: 1.25, spread: 180, gravity: 0.35, drift: 0.8, swirl: 60, stagger: 0.42, fade: 0.42, settle: 0.7, hold: 1.05, smoothing: 0.12, tintA: [1.0, 0.3, 0.0], tintB: [1.0, 0.82, 0.2] });"
    html = html.replace(old_ps_call, new_ps_call)

    # 18. Verify Critical Animations & Handlers are Intact!
    assert 'ParticleScroll.mountParticleScroll' in html, "ERROR: ParticleScroll.mountParticleScroll missing!"
    assert 'ThreeUITerrainPlume.mountTerrainPlume' in html, "ERROR: ThreeUITerrainPlume missing!"
    assert 'signup()' in html, "ERROR: signup() missing!"
    assert 'illParallax()' in html, "ERROR: illParallax() missing!"
    assert 'const els = [...document.querySelectorAll' in html, "ERROR: els declaration missing!"

    # 19. Audit Remaining Sublevel / Porto / Studio Mentions
    sublevel_matches = re.findall(r'.{0,35}sublevel.{0,35}', html, re.IGNORECASE)
    porto_matches = re.findall(r'.{0,35}porto.{0,35}', html, re.IGNORECASE)

    print("--- AUDIT RESULTS ---")
    print(f"Remaining 'sublevel' occurrences: {len(sublevel_matches)}")
    for m in sublevel_matches:
        print("  MATCH:", m.strip())

    print(f"Remaining 'porto' occurrences: {len(porto_matches)}")
    for m in porto_matches:
        print("  MATCH:", m.strip())

    assert len(sublevel_matches) == 0, f"Found {len(sublevel_matches)} remaining sublevel occurrences!"
    assert len(porto_matches) == 0, f"Found {len(porto_matches)} remaining porto occurrences!"

    # Write output file
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Successfully generated: {target_path} ({len(html)} bytes)")

if __name__ == '__main__':
    main()
