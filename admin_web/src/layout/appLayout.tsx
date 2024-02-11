import NavBar from "@/components/navbar";
import Sidebar from "@/components/sidebar";
import { RootState } from "@/redux/store";
import cn from "classnames";
import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { Navigate, useLocation, Outlet } from "react-router-dom";

function AppLayout() {
  const [isOpen, setIsOpen] = useState(false);
  const { pathname } = useLocation();
  const isToggle = () => setIsOpen(!isOpen);

  console.log(pathname);
  // const loginStatus = useSelector<RootState>((state) => state.user.loginStatus);
  const loginStatus = true;
  if (!loginStatus) {
    // console.log("false login");
    return <Navigate to="/login" />;
  }

  if (pathname === "/login" && loginStatus) {
    // console.log("false login");
    return <Navigate to="/dashboard" />;
  }
  console.log("applayout");
  return (
    <>
      <div className="flex">
        <Sidebar isOpen={isOpen} isToggle={isToggle} />
        <div
          className={cn("flex flex-col w-full px-2", {
            "md:ml-72": !isOpen,
            "md:ml-20": isOpen,
          })}
        >
          <NavBar />
          <div className="w-full  overflow-x-none transition translation-all">
            <Outlet />
          </div>
        </div>
      </div>
    </>
  );
}

export default AppLayout;
