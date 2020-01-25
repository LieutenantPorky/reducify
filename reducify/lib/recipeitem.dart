import 'dart:convert';
import 'webservice.dart';


class Recipe {

  final String name;
  final List<String> recipes;

  Recipe({this.name, this.recipes});

  factory Recipe.fromJson(Map<String,dynamic> json) {
    return Recipe(
      name: json['name'],
      recipes: json['recipes'],
    );
  }


  static Resource<List<Recipe>> get all {

     return Resource(
       url: "http://127.0.0.1:5000",
       dest: "recipes",
       parse: (response) {
         final result = jsonDecode(response.body);
         Iterable list = result['data'];
         return list.map((model) => Recipe.fromJson(model)).toList();
       }
     );

     // return [Recipe(name="testItem", date="never",number=5)];

   }
}
