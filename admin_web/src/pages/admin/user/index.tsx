import { useState } from "react";

import AddUserModal from "./components/Modal";

function User() {
  const [isDrawerOpen, setIsModalOpen] = useState(false);

  const toggleModal = () => {
    setIsModalOpen((prevState) => !prevState);
  };

  return (
    <>
      <div className="my-12 px-4 md:px-8 xl:px-12 py-4">
        <div className="flex justify-between items-center">
          <p>Collection center Location</p>
          <button
            onClick={() => setIsModalOpen(true)}
            className="w-fit px-4 primary-btn"
          >
            Add Location
          </button>
        </div>
      </div>

      <AddUserModal isOpen={isDrawerOpen} toggleModal={toggleModal} />
    </>
  );
}

export default User;
