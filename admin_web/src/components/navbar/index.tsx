import UserMenu from "../usermenu";
import NotificationMenu from "../notificationmenu";
import MobileSidebar from "../mobile-sidebar";

const NavBar = () => {
  return (
    <nav className="h-16 w-full ">
      <div className="flex justify-between md:justify-end items-center py-4 px-4">
        <div className="md:hidden">{/* <MobileSidebar /> */}</div>
        <div className="flex gap-3 items-center">
          <NotificationMenu />
          <UserMenu />
        </div>
      </div>
    </nav>
  );
};

export default NavBar;
