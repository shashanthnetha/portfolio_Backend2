import { useState, useEffect, useCallback } from "react";
import { CrtBackground } from "./CrtBackground";
import "./styles.css";

export interface CrtIntroOverlayProps {
  onEnter: () => void;
}

export function CrtIntroOverlay({ onEnter }: CrtIntroOverlayProps) {
  const [isExiting, setIsExiting] = useState(false);

  const triggerEnter = useCallback(() => {
    if (isExiting) return;
    setIsExiting(true);
    setTimeout(() => {
      onEnter();
    }, 650);
  }, [isExiting, onEnter]);

  useEffect(() => {
    // 5-second cinematic countdown (5 -> 4 -> 3 -> 2 -> 1) then transition into website
    const timer = setTimeout(() => {
      triggerEnter();
    }, 5100);

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.code === "Space" || e.code === "Enter" || e.code === "Escape") {
        e.preventDefault();
        triggerEnter();
      }
    };
    window.addEventListener("keydown", handleKeyDown);

    return () => {
      clearTimeout(timer);
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, [triggerEnter]);

  return (
    <div
      className={`crt-intro-overlay ${isExiting ? "is-exiting" : ""}`}
      onClick={triggerEnter}
    >
      <div className="crt-screen-frame">
        <CrtBackground variant="cinematic" speed={1} motion={1} />
      </div>
    </div>
  );
}
