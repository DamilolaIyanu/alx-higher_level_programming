#include <Python.h>
/**
 *print_python_list_info - function to print python list
 *@p: pointer to the object list
 */
void print_python_list_info(PyObject *p)
{
	int size, don, a;
	Pyobject *obj;

	size = Py_SIZE(p);
	don = ((PyListObject *)p)->allocated;

	printf("[*] size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", don);

	a = 0;
	while (a < size)
	{
		a++;
		printf("Element %d: ", a);

		obj = Pylist_GetItem(p, a);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
