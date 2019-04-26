(function(){

  var app = angular.module("ledApp", []);

  var ledController = function($scope,$http){

    var ipaddress = "192.168.0.22:5000";

    $scope.red = 0;
    $scope.green = 0;
    $scope.blue = 0;

    var changeLedColor = function(){
      var cssLedLight = document.getElementsByClassName('led-light')[0];
      cssLedLight.style.backgroundColor = `rgb(${$scope.red},${$scope.green},${$scope.blue})`;
      var url = `http://${ipaddress}/led?r=${$scope.red}&g=${$scope.green}&b=${$scope.blue}`;
      $http.get(url)
        .then(console.log(res));
    }


    $scope.changeLedColor = changeLedColor;

  }


  app.controller('ledController', ["$scope","$http", ledController]);

}());