const TOKEN_KEY = "token";
const USER_DATA_KEY = "user";

interface ISetUserLoginProps {
  isRememberMe: boolean;
  userData: any;
  token: string;
}

export function getToken() {
  const localStorageToken = localStorage.getItem(TOKEN_KEY);
  const sessionStorageToken = sessionStorage.getItem(TOKEN_KEY);

  if (localStorageToken) return localStorageToken;
  if (sessionStorageToken) return sessionStorageToken;
  return null;
}

export function setUserLogin(props: ISetUserLoginProps) {
  const { isRememberMe = false, userData, token } = props;

  if (isRememberMe) {
    localStorage.setItem(USER_DATA_KEY, JSON.stringify(userData));
    localStorage.setItem(TOKEN_KEY, token);
    return;
  }

  sessionStorage.setItem(USER_DATA_KEY, JSON.stringify(userData));
  sessionStorage.setItem(TOKEN_KEY, token);
}

export function getUserData() {
  const localStorageData = localStorage.getItem(USER_DATA_KEY);
  const sessionStorageData = sessionStorage.getItem(USER_DATA_KEY);

  try {
    if (localStorageData) return JSON.parse(localStorageData);
    if (sessionStorageData) return JSON.parse(sessionStorageData);
  } catch {
    return null;
  }
}

export function isUserLogin() {
  const localStorageToken = localStorage.getItem(TOKEN_KEY);
  const sessionStorageToken = sessionStorage.getItem(TOKEN_KEY);
  const userData = getUserData();

  if ((localStorageToken || sessionStorageToken) && userData) return true;
  return false;
}

export function resetUserLogin() {
  const userData = getUserData();
  if (userData) {
    localStorage.clear();
    sessionStorage.clear();
  }
}
