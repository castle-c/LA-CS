app.controller('InfoCtrl', [
    '$scope',
    '$http',
    '$timeout',
  function ($scope, $http, $timeout) {
    let logError = err => console.log("error", err)
    let info = null

    $http.get("http://localhost:8000/info")
         .then((res) => { $scope.info = res.data
          // console.log('info', $scope.info)
          logError
       })

//     $scope.addInfo = (artist) => {
//      $http.post("http://localhost:8000/info", {artist_name: artist})
//          .then((res) => { $scope.info = res.data
//           logError
//        })
//           .then(
//             res => {
//               $scope.info.push(res.data);
//               $scope.newInfo = "";
//               $timeout()
//             }
//           )
//       } else {
//         alert("Artist is blank!")
//       }
//     }
// }])
