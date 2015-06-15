(function(){
	var app = angular.module('flavors', []);
	
	app.controller('FlavorController', ['$http', '$log', '$scope', function($http, $log, $scope){
		this.loadFlavors = function(url){
			url = url || "/api/v1/flavors/";
			$http.get(url)
			.success(function(response) {
	    		flavors = response['results'];
	    		flavors.forEach(function(flavor){
	    			$http.get(flavor.source).success(function(data){
	    				flavor.name = flavor.name + ' - ' + data.name
	    			});
	    		});
	    		$scope.flavors = $scope.flavors.concat(flavors);
	    		if (response.next != null){
					$scope.loadFlavors(response.next);
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

		$scope.flavors = [];
		this.loadFlavors();
	} ]);
})();