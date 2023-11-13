#include <Python.h>
/**
 *print_python_list_info - prints list info
 *
 *@p: thepointer to the list
 */
void print_python_list_info(PyObject *p)
{
	int size, i, alloc;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
	}
}
