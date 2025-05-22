from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_price',
            new_name='unit_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='desciption',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='promotion',
            old_name='discription',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='promotion',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AddConstraint(
            model_name='cartitem',
            constraint=models.UniqueConstraint(fields=('cart', 'product'), name='unique_cart_product'),
        ),
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('order', 'product'), name='unique_order_product'),
        ),
    ] 