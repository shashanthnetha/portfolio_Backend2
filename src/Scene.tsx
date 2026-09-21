import { useState } from "react";
import { CrtIntroOverlay } from "./effects/crt/CrtIntroOverlay";

export function SublevelStudioLandingPage() {
  return (
    <div
      className="threeui-background landing-page-frame"
      style={{
        position: "relative",
        width: "100%",
        height: "100%",
        overflow: "hidden",
        background: "#080808",
      }}
    >
      <iframe
        title="Shashanth Pittala — AI & Systems Engineer"
        src="./landing-pages/sublevel-studio.html"
        sandbox="allow-downloads allow-forms allow-modals allow-popups allow-same-origin allow-scripts"
        loading="eager"
        style={{
          position: "absolute",
          inset: 0,
          width: "100%",
          height: "100%",
          border: 0,
          display: "block",
        }}
      />
    </div>
  );
}

export function Scene() {
  const [showIntro, setShowIntro] = useState(true);

  return (
    <div className="shader-frame" style={{ position: "relative", width: "100%", height: "100%" }}>
      {/* Background 3D Portfolio preloads immediately */}
      <SublevelStudioLandingPage />

      {/* Pure Cinematic CRT Loading Screen */}
      {showIntro && (
        <CrtIntroOverlay onEnter={() => setShowIntro(false)} />
      )}
    </div>
  );
}
