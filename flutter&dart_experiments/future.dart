// Dart has a Future type. A Future in Dart is an object that represents the result of an asynchronous operation.
// It's a promise that a value or an error will be available at some point in the future.
// Futures are commonly used for tasks that take time to complete, such as network requests, file I/O operations, or accessing a database

// This example shows how *not* to write asynchronous Dart code.

Future<String> createOrderMessage() async {
  print('Awaiting user order...');
  var order = await fetchUserOrder();
  return 'Your order is: $order';
}

Future<String> fetchUserOrder() =>
    // Imagine that this function is more complex and slow.
    Future.delayed(const Duration(seconds: 6), () => 'Large Latte');

Future<void> main() async {
  countSeconds(6);
  print(await createOrderMessage());
}

void countSeconds(int s) {
  for (int i = 1; i <= s; i++) {
    Future.delayed(Duration(seconds: i), () => print(i));
    // sleep(Duration(seconds: 1)); if we use sleep then it blocks the entire flow
  }
}

// output for the above is =>  Your order is: Instance of '_Future<String>'
// fetchUserOrder() is an asynchronous function that, after a delay, provides a string that describes the user's order: a "Large Latte".
// To get the user's order, createOrderMessage() should call fetchUserOrder() and wait for it to finish. Because createOrderMessage() does not wait for fetchUserOrder() to finish, createOrderMessage() fails to get the string value that fetchUserOrder() eventually provides.
// A future (lower case "f") is an instance of the Future (capitalized "F") class. A future represents the result of an asynchronous operation, and can have two states: uncompleted or completed.
// When you call an asynchronous function, it returns an uncompleted future. That future is waiting for the function's asynchronous operation to finish or to throw an error.
// A future of type Future<T> completes with a value of type T. For example, a future with type Future<String> produces a string value. If a future doesn't produce a usable value, then the future's type is Future<void>.

// Future<void> fetchUserOrder() {
//   // Imagine that this function is fetching user info but encounters a bug.
//   return Future.delayed(
//     const Duration(seconds: 2),
//     () => throw Exception('Logout failed: user ID is invalid'),
//   );
// }

// void main() {
//   fetchUserOrder();
//   print('Fetching user order...');
// }


// A Future<T> instance produces a value of type T.
// If a future doesn't produce a usable value, then the future's type is Future<void>.
// A future can be in one of two states: uncompleted or completed.
// When you call a function that returns a future, the function queues up work to be done and returns an uncompleted future.
// When a future's operation finishes, the future completes with a value or with an error.