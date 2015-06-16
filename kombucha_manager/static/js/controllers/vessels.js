(function(){
	var app = angular.module('vessels', []);
	
	app.controller('VesselController', ['$http', '$log', '$scope', function($http, $log, $scope){
		$scope.loadVessels = function(url){
			url = url || "/api/v1/vessels/";
			$scope.vessels = [];
			$scope.vesselLoader = $http.get(url)
			.success(function(response) {
				$scope.vessels = $scope.vessels.concat(response.results);
				if (response.next != null){
					loadVessels(response.next);
				}
	    	})
	    	.error(function(response, status, headers, config) {
	    		if (status == 403) {
	    			$('#loginModal').on('shown.bs.modal', function () {
	  					$('#username').focus()
					})
	    			$('#loginModal').modal('show');
	    		}
	    	});
		};
		$scope.vessels = [];
		$scope.loadVessels();
	} ]);
})();
