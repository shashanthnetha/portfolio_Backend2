import { useEffect, useRef } from "react";
import { createCrtRenderer, crtStyle, CRT_DEFAULTS, CRT_VARIANTS, type CrtOptions } from "./crtRenderer";
import type { CrtVariant } from "./crtScreens";

export { CRT_VARIANTS };
export type { CrtVariant };
export type CrtBackgroundProps = Partial<CrtOptions> & { className?: string };

export function CrtBackground({ className = "", ...props }: CrtBackgroundProps) {
  const hostRef = useRef<HTMLDivElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const optionsRef = useRef({ ...CRT_DEFAULTS, ...props });
  optionsRef.current = { ...CRT_DEFAULTS, ...props };

  useEffect(() => {
    const host = hostRef.current;
    const canvas = canvasRef.current;
    if (!host || !canvas) return undefined;

    const renderer = createCrtRenderer(host, canvas, () => optionsRef.current);
    let frame = 0;
    let visible = true;

    const resize = () => {
      renderer.resize();
      renderer.render(performance.now());
    };

    const tick = (now: number) => {
      renderer.render(now);
      frame = visible && !document.hidden ? requestAnimationFrame(tick) : 0;
    };

    const resizeObserver = new ResizeObserver(resize);
    const intersection = new IntersectionObserver(([entry]) => {
      visible = entry?.isIntersecting ?? true;
      if (visible && !frame) frame = requestAnimationFrame(tick);
      if (!visible && frame) {
        cancelAnimationFrame(frame);
        frame = 0;
      }
    });

    resizeObserver.observe(host);
    intersection.observe(host);
    resize();
    frame = requestAnimationFrame(tick);

    return () => {
      if (frame) cancelAnimationFrame(frame);
      resizeObserver.disconnect();
      intersection.disconnect();
      renderer.dispose();
    };
  }, []);

  const options = { ...CRT_DEFAULTS, ...props };
  return (
    <div
      ref={hostRef}
      className={`threeui-background crt crt-${options.variant}${className ? ` ${className}` : ""}`}
      style={{
        background: crtStyle(options.variant).background,
        opacity: options.opacity,
        filter: `hue-rotate(${options.hue}deg) saturate(${options.saturation}) brightness(${options.brightness})`,
      }}
    >
      <canvas ref={canvasRef} />
    </div>
  );
}
