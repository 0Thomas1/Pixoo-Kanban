# Pixoo Kanban

Pixoo Kanban is a project management tool designed to display your kanban board on a Pixoo 64 device.
Thanks to [SomethingWithComputers](https://github.com/SomethingWithComputers) for his [pixoo](https://github.com/SomethingWithComputers/pixoo) API.

## Features


- **Kanban Board**: Visualize tasks in different stages of completion.
- **Customizable Colors**: Customize colors to your liking

## Installation

1. Clone the repository:
  ```sh
  git clone https://github.com/0Thomas1/Pixoo-Kanban.git
  ```
2. Navigate to the project directory:
  ```sh
  cd pixoo-kanban
  ```
3. Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```
## Prequisite
  The MongoDB containing the tasks is from one of my other project [kanban](https://github.com/0Thomas1/kanban). This program can only work on a DB with the same document.

  The Schema are as follows:

  tasks:
  ```js
  const taskSchema = new mongoose.Schema({
  title: String,
  description: String,
  taskStatus: String,
  createdAt: {
    type: Date,
    immutable: true,
    default: () => Date.now(),
  },
  updatedAt: Date,
  user: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User",
  },
  });
  ```

  users:

  ```js
  const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String,
  tasks: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: "Task",
  }],
  createdAt: {
    type: Date,
    immutable: true,
    default: () => Date.now(),
  },
  updatedAt: {
    type: Date,
    default: () => Date.now(),
  },
  });
  ```

## Usage

1. To start:
  ```sh
  python ./src/driver.py
  ```



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

