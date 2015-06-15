(function(){
	var app = angular.module('teas', []);
	
	app.controller('TeaController', ['$http', '$log', '$scope', function($http, $log, $scope){
		this.loadTeas = function(url){
			url = url || "/api/v1/teas/";
			$http.get(url)
			.success(function(response) {
	    		$scope.teas = response['results'];
	    	})
	    	.error(function(response, status, headers, config) {
	    		if (status == 403) {
	    			$('#loginModal').on('shown.bs.modal', function () {
	  					$('#username').focus()
					})
	    			$('#loginModal').modal('show');
	    		}
	    	});

			this.joinNames = function(objects){
				var return_str = "";

				angular.forEach(objects, function(object){
					return_str = return_str + object.name + ' ';
				});

				return return_str;
			};
		};

		this.loadTeas();
	} ]);
})();