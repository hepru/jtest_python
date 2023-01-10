from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO menu_treemenucategory (id, name) 
                VALUES (1, 'main_menu');
            
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (1, 'Home', 'home', 1, null);
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (2, 'About', 'about', 1, null);
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (3, 'Development', 'development', 1, null);
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (4, 'Development C#', 'development_csharp', 1, 3);
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (5, 'Development Python', 'development_python', 1, 3);
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (6, 'Development Python/Django', 'development_python_django', 1, 6);
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (7, 'Development Python/Fast API', 'development_python_fast_api', 1, 6);
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (8, 'Prices', 'prices', 1, null);
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (9, 'GitHub', 'https://github.com/hep1984/', 1, 3);

            INSERT INTO menu_treemenucategory (id, name) 
                VALUES (2, 'second_menu');
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (10, 'Tests', 'tests', 2, null);
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (11, 'Test1', 'test1', 2, 10);
            INSERT INTO menu_treemenu (id, name, link, category_id, parent_id) 
                VALUES (12, 'Test2', 'test2', 2, 10);
            
            ALTER TABLE menu_treemenucategory ALTER COLUMN id RESTART WITH 3;
            ALTER TABLE menu_treemenu ALTER COLUMN id RESTART WITH 13;
        """)
    ]
