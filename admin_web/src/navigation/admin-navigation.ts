import {
  Squares2X2Icon,
  UsersIcon,
  BuildingStorefrontIcon,
  ChatBubbleOvalLeftEllipsisIcon,
  InformationCircleIcon,
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

export const customerCareLink: INavigation[] = [
  {
    id: "help-center",
    name: "Help center",
    path: "/help-center",
    icon: InformationCircleIcon,
  },
  {
    id: "contact-us",
    name: "Contact us",
    path: "/contact-us",
    icon: ChatBubbleOvalLeftEllipsisIcon,
  },
];
