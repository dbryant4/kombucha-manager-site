(function(){
	var app = angular.module('sizes', []);
	
	app.controller('SizeController', ['$http', '$log', '$scope', function($http, $log, $scope){
		this.loadSizes = function(url){
			url = url || "/api/v1/bottle-sizes/";
			$http.get(url)
			.success(function(response) {
	    		sizes = response['results'];
	    		$scope.sizes = $scope.sizes.concat(sizes);
	    		if (response.next != null){
					$scope.loadSizes(response.next);
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

		$scope.sizes = [];
		this.loadSizes();
	} ]);
})();