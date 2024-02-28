import os
#This is to clear all migrations,pycache and database to clear out everything when we have messed up with the model configuration
def clear_pycache_migrations_and_db():
    root_dir = os.getcwd() 
    for root, dirs, files in os.walk(root_dir):
        for directory in dirs:
            if directory == '__pycache__':
                pycache_dir = os.path.join(root, directory)
                print(f"Removing {pycache_dir}...")
                try:
                    os.system(f"rm -rf {pycache_dir}")
                except Exception as e:
                    print(f"Error removing {pycache_dir}: {str(e)}")
            if directory == 'migrations':
                migration_dir = os.path.join(root, directory)
                for migration_file in os.listdir(migration_dir):
                    if migration_file != '__init__.py' and migration_file.endswith('.py'):
                        migration_path = os.path.join(migration_dir, migration_file)
                        print(f"Removing {migration_path}...")
                        try:
                            os.remove(migration_path)
                        except Exception as e:
                            print(f"Error removing {migration_path}: {str(e)}")
        for file in files:
            if file == 'db.sqlite3':
                db_file = os.path.join(root, file)
                print(f"Removing {db_file}...")
                try:
                    os.remove(db_file)
                except Exception as e:
                    print(f"Error removing {db_file}: {str(e)}")

clear_pycache_migrations_and_db()