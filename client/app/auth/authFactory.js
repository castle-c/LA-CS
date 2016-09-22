app.factory('AuthFactory', [
    '$cookies', '$location',
    ($cookies, $location) => {
      let userCredentials = null;

      return {
        credentials (creds) {
          if (creds) {
            userCredentials = window.btoa(`${creds.username}:${creds.password}`);
            $cookies.put('rest', userCredentials);
          } else {
            return userCredentials;
          }
        },
        logout () {
          userCredentials = null;
          $cookies.remove('rest');
          $location.path("/login");
        },
        read () {
          return userCredentials = $cookies.get('rest');
        },
        update (creds) {
          userCredentials = creds;
        }
      }
    }
  ]);
