with open('menu.html', 'r') as f:
    content = f.read()

# Instead of using eval, we can just set data attributes on the add button and let a global handler deal with it.
# Actually, the original implementation had this for all pizzas:
# <button id="add-btn-1" onclick="alert('Seleccione un tamaño antes de agregar al carrito')" ...>
# So they are un-clickable until a size is selected!
# "If a pizza has a pre-selected default size on page load, a user can click "Agregar" directly"
# The reviewer states this, let's verify if there are pre-selected sizes.
import re

pizzas_with_add = re.findall(r'<button id="add-btn-(\d+)" onclick="(.*?)"', content)
for pid, onclick in pizzas_with_add:
    print(f"Pizza {pid}: {onclick}")
