(function(){
	var app = angular.module('kombucha_manager', ['batches', 'bottles', 'vessels', 'teas', 'panels', 'sizes', 'flavors', 'authentication', 'angular-loading-bar', 'smart-table'])
	.config(['cfpLoadingBarProvider', '$httpProvider', function(cfpLoadingBarProvider, $httpProvider) {
    	cfpLoadingBarProvider.includeSpinner = false;
    	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
    	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  	}]);

	
	
})();