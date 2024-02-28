import {
  Squares2X2Icon,
  UsersIcon,
  BuildingStorefrontIcon,
} from "@heroicons/react/24/outline";

interface INavigation {
  id: string;
  name: string;
  path: string;
  icon: React.ForwardRefExoticComponent<
    Omit<React.SVGProps<SVGSVGElement>, "ref"> & {
      title?: string | undefined;
      titleId?: string | undefined;
    } & React.RefAttributes<SVGSVGElement>
  >;
}

export const navigationLinks: INavigation[] = [
  {
    id: "dashboard",
    name: "Dashboard",
    path: "/dashboard",
    icon: Squares2X2Icon,
  },

  {
    id: "users",
    name: "Users",
    path: "/user",
    icon: UsersIcon,
  },
  {
    id: "pickups",
    name: "Pickers",
    path: "/picker",
    icon: BuildingStorefrontIcon,
  },
];
