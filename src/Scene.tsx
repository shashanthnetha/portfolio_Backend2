import { useState } from "react";
import { SublevelStudioLandingPage } from "@designcodeio/threeui";
import "@designcodeio/threeui/style.css";
import { CrtIntroOverlay } from "./effects/crt/CrtIntroOverlay";

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
