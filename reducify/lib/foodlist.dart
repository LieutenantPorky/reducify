import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'fooditem.dart';
import 'dart:convert';
import 'webservice.dart';


class IngredientListState extends State<IngredientList> {

  List<Ingredient> _ingredients = List<Ingredient>();

  @override
  void initState() {
    super.initState();
    _populateIngredients();
  }

  void _populateIngredients() {

    Webservice().load(Ingredient.all).then((ingredients) => {
  setState(() => {
    _ingredients = ingredients
  })
});

    // Webservice().load(Ingredient.all).then((ingredients) => {
      // setState(() => {
      //   _ingredients = [
      //     Ingredient(name:"testItem", date:"never",number:5),
      //     Ingredient(name:"Cookies", date:"never",number:200),
      //   ],
      //   token="putTokenHere"
      // });
    // });


  }

  Card _buildItemsForListView(BuildContext context, int index) {
     return Card(
       child: ListTile(
         title: Center(
           child: Text(_ingredients[index].name, style: TextStyle(fontSize: 20)),
         ),
         subtitle: Center(
           child: Text("quantity: ${_ingredients[index].number.toString()}", style: TextStyle(fontSize: 18))
         ),
       )
     );
 }


  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: _ingredients.length,
      itemBuilder: _buildItemsForListView,
    );
  }
}

class IngredientList extends StatefulWidget {

  @override
  createState() => IngredientListState();
}
