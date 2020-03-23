var app = angular.module("leagueStats", []);
app.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});
app.controller("leagueStatsController", function($scope, $http, $sce, $timeout) {

	$scope.message = {};
	$scope.message_status = {};
	$scope.show = false;
	
	$scope.saveForm = function() {
		var data = {
			nombre: $scope.nombre,
			paterno: $scope.paterno,
			materno: $scope.materno,
			run: $scope.run,
			fechanacimiento: $scope.fechanacimiento,
			telefono: $scope.telefono,
			correo: $scope.correo,
			especialidad_medica: $scope.especialidad_medica,
			medico: $scope.medico,
			modalidad_de_atencion: $scope.modalidad_de_atencion,
			razonconsulta: $scope.razonconsulta,
		}
		if (data) {
			$http.post('/api/exam_form/', data).then(function successCallback(response) {
				$scope.message = "Formulario enviado con éxito.";
				$scope.message_status = 1;
				$scope.show = true;
			}, function errorCallback(response) {
				if (response.status == 404) {
					$scope.message = "Debe llenar todos los campos obligatorios.";
					$scope.message_status = 2;
					$scope.show = true;
				}
				else {
					$scope.message = "Ha ocurrido un error, por favor, envie el formulario nuevamente.";
					$scope.message_status = 3;
					$scope.show = true;
				}
			});
		}
		else {
			console.log("not_ready");
		}
		
	};   
});