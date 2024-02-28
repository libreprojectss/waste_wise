import { Bars3CenterLeftIcon } from "@heroicons/react/24/outline";
import cn from "classnames";

import { useEffect, useState } from "react";

export default function MobileSidebar() {
  // for handling hydration error
  const [isMounted, setIsMounted] = useState(false);

  useEffect(() => {
    setIsMounted(true);
  }, []);
  if (!isMounted) return null;

  const [isMobile, setIsMobile] = useState(false);
  const isMobileFun = () => {
    setIsMobile((pre) => !pre);
  };

  return (
    <div>
      <div>
        <Bars3CenterLeftIcon width={24} height={24} onClick={isMobileFun} />
      </div>
      <div
        className={cn("z-10  h-screen bg-white transition-all shadow-md", {
          hidden: isMobile,
        })}
      ></div>
    </div>
  );
}
