import 'package:flutter/material.dart';
import 'package:flutter/semantics.dart';
// import 'webservice.dart';
import 'foodlist.dart';
import 'recipelist.dart';
import 'images.dart';
import 'package:flutter/foundation.dart'
    show debugDefaultTargetPlatformOverride;
void main() {
  debugDefaultTargetPlatformOverride = TargetPlatform.fuchsia;
  runApp(new MyApp());
}
class MyApp extends StatelessWidget {


  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Reducify test",
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: HomePage(),
    );
  }
}

class RecipePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Recipes you can cook"),
        centerTitle: true,
      ),
      body:  RecipeList(),
      bottomNavigationBar: BottomAppBar(
        color: Colors.grey,
        shape: const CircularNotchedRectangle(),
        child: Container(
          height: 50.0,
        ),
      ),
      // floatingActionButton: FloatingActionButton(
      //   onPressed: () {
      //     Navigator.pop(context);
      //   },
      //   tooltip: 'Go back',
      //   child: Icon(Icons.cake),
      // ),
      // floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
    );
  }
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Ingredients in your fridge"),
        centerTitle: true,
        actions: <Widget> [
          IconButton(
            icon: const Icon(Icons.camera_alt),
            tooltip: "upload receipt",
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => ReceiptUpload()),
              );
            },
          ),
        ],
      ),
      body: IngredientList(),
      bottomNavigationBar: BottomAppBar(
        color: Colors.grey,
        shape: const CircularNotchedRectangle(),
        child: Container(
          height: 50.0,
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => RecipePage()),
          );
        },
        tooltip: 'Find Recipes',
        child: Icon(Icons.cake),
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
    );
  }
}

class ReceiptUpload extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("select a receipt"),
        centerTitle: true,
      ),
      body: Text("image picker"),
    );
  }
}
