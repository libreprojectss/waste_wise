import { Fragment } from "react";

import { Menu, Transition } from "@headlessui/react";
import { ChevronDownIcon } from "@heroicons/react/24/solid";
import { useSelector } from "react-redux";

export default function UserMenu() {
  const { user } = useSelector((state: any) => state.user);
  return (
    <div className="w-fit">
      <Menu as="div" className="relative inline-block text-left">
        <div className="flex gap-x-3">
          <div className="basis-8 aspect-square  ring-core-primary object-cover w-8 h-8 text-center bg-gray-300 rounded-full cursor-pointer">
            <img
              src="https://xsgames.co/randomusers/avatar.php?g=male"
              alt=""
              className=" rounded-full"
            />
          </div>
          <Menu.Button>
            <div className="flex gap-x-1 items-center">
              <p>{"John"}</p>
              <ChevronDownIcon width={20} height={20} />
            </div>
          </Menu.Button>
        </div>
        <Transition
          as={Fragment}
          enter="transition ease-out duration-100"
          enterFrom="transform opacity-0 scale-95"
          enterTo="transform opacity-100 scale-100"
          leave="transition ease-in duration-75"
          leaveFrom="transform opacity-100 scale-100"
          leaveTo="transform opacity-0 scale-95"
        >
          <Menu.Items className="ring-1 ring-black ring-opacity-5 focus:outline-none absolute right-0 w-56 mt-2 origin-top-right bg-white divide-y divide-gray-100 rounded-md shadow-lg">
            <div className=" px-1 py-1">
              <Menu.Item>
                {({ active }) => (
                  <div>
                    <div>Name</div>
                    <div>Setting</div>
                  </div>
                )}
              </Menu.Item>
            </div>
          </Menu.Items>
        </Transition>
      </Menu>
    </div>
  );
}
