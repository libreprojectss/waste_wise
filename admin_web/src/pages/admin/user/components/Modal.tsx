import Modal, { IModalProps } from "@/components/ui/modal";
import { XMarkIcon } from "@heroicons/react/24/solid";
import AddUserForm from "./Form";

function AddUserModal({ isOpen, toggleModal }: IModalProps) {
  return (
    <Modal isOpen={isOpen} toggleModal={toggleModal} className="max-w-[800px]">
      <div className="flex justify-between items-center">
        <p className="title-section">Add Location Details</p>
        <div
          onClick={toggleModal}
          className="p-1 rounded-full cursor-pointer bg-neutral-50"
        >
          <XMarkIcon height={24} width={24} />
        </div>
      </div>
      <AddUserForm toggleModal={toggleModal} className="" />
    </Modal>
  );
}

export default AddUserModal;
