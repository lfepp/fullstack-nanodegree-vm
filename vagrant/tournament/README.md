# Swiss Pairings

Keep track of players and matches in a Swiss Pairings tournament

## Usage

1. Clone the repository:

    ```
    git clone git@github.com:lfepp/fullstack-nanodegree-vm.git
    ```

1. Change directory to the `tournament` directory:

    ```
    cd vagrant/tournament
    ```

1. Power up the vagrant virtual machine

    ```
    vagrant up    
    ```

1. Log into the vagrant virtual machine

    ```
    vagrant ssh
    ```

1. Change directory to the shared `/vagrant` folder:

    ```
    cd /vagrant
    ```

1. Launch the PostgreSQL command line interface:

    ```
    psql
    ```

1. Create the `tournament` database:

    ```
    CREATE DATABASE tournament;
    ```

1. Connect to the tournament database:

    ```
    \c tournament
    ```

1. Create the database tables using `tournament.sql`:

    ```
    \i tournament/tournament.sql
    ```

1. All commands needed for a tournament can be found in `tournament/tournament.py`

1. Run the following command to exit the PostgreSQL CLI:

    ```
    \q
    ```

## Testing

1. Connect to the PostgreSQL CLI, create the `tournament` database, and create the database tables using the steps outlined in the **Usage** section above

1. Run the test suite in `tournament_test.py`:

    ```
    python tournament/tournament_test.py
    ```

## Author

Luke Epp <lucasfepp@gmail.com>
