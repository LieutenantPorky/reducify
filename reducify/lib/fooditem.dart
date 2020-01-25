import 'dart:convert';
import 'webservice.dart';


class Ingredient {

  final String name;
  final String date;
  final int number;

  Ingredient({this.name, this.date, this.number});

  factory Ingredient.fromJson(Map<String,dynamic> json) {
    return Ingredient(
      name: json['item'],
      date: json['date'],
      number: json['number'],
    );
  }


  static Resource<List<Ingredient>> get all {

     return Resource(
       url: "http://127.0.0.1:5000",
       dest: "fridge",
       parse: (response) {
         final result = jsonDecode(response.body);
         Iterable list = result['data'];
         return list.map((model) => Ingredient.fromJson(model)).toList();
       }
     );

     // return [Ingredient(name="testItem", date="never",number=5)];

   }
}
