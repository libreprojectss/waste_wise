import { PencilSquareIcon, TrashIcon } from "@heroicons/react/24/outline";
import { Link } from "react-router-dom";

const tableHeader = [
  {
    id: 1,
    name: "Full Name",
  },
  {
    id: 2,
    name: "Orders",
  },
  {
    id: 3,
    name: "Payment",
  },
  {
    id: 4,
    name: "Actions",
  },
];
function User() {
  return (
    <>
      <div className="w-full">
        <div className="flex justify-between w-full gap-4 my-8">
          <h1 className="mb-4 text-lg md:text-xl text-core-secondary font-bold">
            List of Users
          </h1>
          <Link to="/course/create">
            <button type="button" className="primaryButton">
              Create
            </button>
          </Link>
        </div>
        <div className="p-4 border border-dashed bg-clip-border rounded-2xl border-stone-200 bg-light/30">
          <div className="flex justify-between w-full gap-4 ">
            <div className="w-1/4">
              <form>
                <label className="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">
                  Search
                </label>
                <input
                  type="search"
                  id="search"
                  className="px-4 py-2 outline-none rounded-lg w-full text-sm text-gray-900 border border-gray-300 "
                  placeholder="Search"
                  required
                />
              </form>
            </div>
          </div>
          <table width="100%">
            <thead className="border-none">
              <tr className="">
                {tableHeader.map((head) => {
                  return (
                    <th className="tableHead" key={head.id}>
                      {head.name}
                    </th>
                  );
                })}
              </tr>
            </thead>

            <tbody className="">
              {/* {tableData && */}
              {/* tableData.map((data, i) => { */}
              {/* return ( */}
              <tr className={` ${1 % 2 === 0 && "bg-gray-100"}`}>
                <td className="tableData">
                  <div className="flex items-center">
                    <div className="relative inline-block shrink-0 rounded-2xl me-3">
                      <img
                        src="https://raw.githubusercontent.com/Loopple/loopple-public-assets/main/riva-dashboard-tailwind/img/img-49-new.jpg"
                        className="w-[50px] h-[50px] inline-block shrink-0 rounded-2xl"
                        alt=""
                      />
                    </div>
                    <p>Name of User</p>
                  </div>
                  {/* {data?.image && (
                  <img src={data?.image} width={90} height={90} />
                )} */}
                </td>

                <td className="tableData truncate">
                  {/* {data?.category?.name} */}
                </td>
                <td className="tableData truncate">
                  {/* {data?.category?.name} */}
                </td>
                <td className="tableData">
                  <div className="tableDataActionContainer">
                    <div
                      // onClick={() =>
                      //   navigate(`/course/edit/${data?.id}/editCourse`)
                      // }
                      className="tableActionContainer"
                    >
                      <PencilSquareIcon className="tableEditIcon" />
                    </div>
                    <div
                      // onClick={() => {
                      //   onOpen();
                      //   setSelectedId(data?.id);
                      // }}
                      className="tableActionContainer"
                    >
                      <TrashIcon className="tableDeleteIcon " />
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </>
  );
}

export default User;
