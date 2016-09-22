'use strict'

  app.config($routeProvider => {
    $routeProvider
      .when('/parishes', {
        controller: 'ParishesCtrl',
        templateUrl: '/app/parishes/parishes.html'
      })
      .when('/parishes/:parishId', {
        controller: 'ParishDetailCtrl',
        templateUrl: '/app/parishes/parishDetail.html'
      })

});

