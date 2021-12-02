# android-permissions

Write a program that automatically identifies the dangerous permissions in all methods in all Java programs in the directory FARMING_ANDROID_REPOS/. Check https://developer.android.com/training/permissions/requesting on how Android permissions are specified in Java programs. You will need traverse the AST of Java programs. If you are using Python then you will find the https://github.com/c2nes/javalang library helpful. If you are using Java, then you can use javac (http://openjdk.java.net/groups/compiler/) or Antlr (https://dzone.com/articles/parsing-any-language-in-java-in-5-minutes-using-an). Simple case sensitive pattern matching would suffice to detect permissions within methods. Here is an example how permissions are specified in Java methods:


Calculate the lines of code for all Java and AndroidManifest.xml files in FARMING_ANDROID_REPOS/
Create a comma separated value (CSV) file called Workshop#5.Output.csv, which will have the following columns:

