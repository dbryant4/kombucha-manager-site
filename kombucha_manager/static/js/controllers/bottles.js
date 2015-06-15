(function(){
	var app = angular.module('bottles', []);
	

	app.controller('BottleController', ['$http', '$log', '$scope', function($http, $log, $scope){
		$scope.loadBottles = function(url){
			url = url || "/api/v1/bottles/";
			$http.get(url)
			.success(function(response) {
	    		$scope.bottles = $scope.bottles.concat(response.results);
	    		if (response.next != null){
					$scope.loadBottles(response.next);
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
    	
    	$scope.bottles = [];
    	$scope.loadBottles();
	} ]);
})();