
  app.config($routeProvider => {
    $routeProvider
      .when('/companies', {
        controller: 'CompaniesCtrl',
        templateUrl: '/app/companies/companies.html'
      })
    .when('/companies/:companyId', {
        controller: 'CompanyDetailCtrl',
        templateUrl: '/app/companies/companyDetail.html'
      })

});
