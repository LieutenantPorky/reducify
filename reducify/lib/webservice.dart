import 'package:http/http.dart' as http;
import 'package:http/http.dart';
import 'dart:convert';

class Resource<T> {
  final String url;
  final String dest;
  T Function(Response response) parse;

  Resource({this.url,this.parse, this.dest});
}

class Webservice {

  Future<T> load<T>(Resource<T> resource) async {
    Map<String, String> headers = {"Content-type": "application/json"};
    String json = '{"username": "Einstein", "password": "mc2"}';
    String tokenTest = "";
    String url = resource.url;
    Response responseTok = await post("$url/auth", headers: headers, body: json);

    if(responseTok.statusCode == 200) {
        tokenTest = jsonDecode(responseTok.body)["access_token"];
        print(tokenTest);
      } else {
        throw Exception('Failed to load Token!');
      }

      Response response = await get("$url/${resource.dest}", headers: {"Authorization": "JWT $tokenTest"});

      if(response.statusCode == 200) {
          return resource.parse(response);
        } else {
          throw Exception('Failed to load data!');
        }


    // if(response.statusCode == 200) {
    //     return resource.parse(response);
    //   } else {
    //     throw Exception('Failed to load data!');
    //   }
  }

}
