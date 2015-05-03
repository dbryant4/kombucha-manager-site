(function(){
	var app = angular.module('kombucha_manager', []);

	app.controller('ManagerController', function(){
		this.tea_types = tea_types;
	});

	app.controller('PanelController', function(){
		this.tab = 'brews'; // Default tab

		this.selectTab = function(setTab){
			this.tab = setTab;
		};

		this.isSelected = function(checkTab){
			return this.tab === checkTab;
		};
	});

	app.controller('BrewsController', function(){
		this.batches = brews

		
	});

	var brews = {
	    "count": 1,
	    "next": null,
	    "previous": null,
	    "results": [
	        {
	            "tea": [
	                "https://kombucha-manager.herokuapp.com/api/v1/teas/3/"
	            ],
	            "tea_volume": "5.0",
	            "sugar_volume": "1.00",
	            "brew_volume": "1.00",
	            "scoby_count": 2,
	            "brew_date": "2015-04-22",
	            "comments": "",
	            "vessel": [
	                "https://kombucha-manager.herokuapp.com/api/v1/vessels/1/"
	            ]
	        }
	    ]
	}

	var tea_types = [
		{
			name: 'Green',
		},
		{
			name: 'White',
		},
		{
			name: 'Black',
		}
	];
})();
