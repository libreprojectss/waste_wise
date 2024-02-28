import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";
import { useForm, SubmitHandler } from "react-hook-form";

import useLoginMutation from "@/services/auth/use-login-mutation";
import { useNavigate } from "react-router-dom";

interface IFormInput {
  email: string;
  password: string;
  isRememberMe?: boolean;
}

//Validate an input value
const schema = yup
  .object({
    email: yup
      .string()
      .email("Email must be valid.")
      .required("Email is required."),
    password: yup.string().required("Password is required."),
    isRememberMe: yup.boolean(),
  })
  .required();

function Login() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
  });

  const { mutate: login, isPending } = useLoginMutation();

  const handleLogin: SubmitHandler<IFormInput> = (data) => {
    login(data);
    // reset();
  };

  return (
    <section className="min-h-screen flex justify-center items-center">
      <div className="min-w-[480px] p-12 rounded-[32px] shadow-2xl bg-white">
        <div className="text-center">
          <h2 className="large-title text-core-indigo">Wastewise</h2>
        </div>

        <form className="mt-6" onSubmit={handleSubmit(handleLogin)}>
          <fieldset>
            <label htmlFor="email" className="label">
              Email
            </label>
            <input
              {...register("email")}
              type="email"
              className="input"
              id="email"
              placeholder="Enter your email"
            />
            {errors.email && (
              <p className="mt-2 text-sm text-red-500">
                {errors.email.message}
              </p>
            )}
          </fieldset>

          <fieldset className="mt-4">
            <label htmlFor="password" className="label">
              Password
            </label>

            <input
              {...register("password")}
              type="show ? 'password' : 'text'"
              className="input"
              id="password"
              placeholder="Enter your password"
            />
            {errors.password && (
              <p className="mt-2 text-sm text-red-500">
                {errors.password.message}
              </p>
            )}
          </fieldset>

          <div className="mt-4">
            <div className="flex gap-2">
              <input
                {...register("isRememberMe")}
                type="checkbox"
                className="cursor-pointer"
              />
              <label>Remember me</label>
            </div>
          </div>

          <button
            disabled={isPending}
            type="submit"
            className="primary-btn bg-core-indigo mt-8"
          >
            Login
          </button>
        </form>
      </div>
    </section>
  );
}

export default Login;
