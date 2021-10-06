#include <dshow.h>
#include <Python.h>
#include "playback.h"

// Variable pour contr�ler le vid�o player
DShowPlayer* g_pPlayer = NULL;

// G�re les entr�es claviers re�ues
void ManageInput(char ch)
{
	switch (ch)
	{
	case L'p':
	case L'P':
		if (g_pPlayer->State() == STATE_RUNNING)
		{
			g_pPlayer->Pause();
		}
		else
		{
			g_pPlayer->Play();
		}
		break;
	case L'a':
	case L'A':
		g_pPlayer->FastForward();
		break;
	case L'r':
	case L'R':
		g_pPlayer->Back();
		break;
	case L'q':
	case L'Q':
		delete g_pPlayer;
		exit(0);
		break;
	}
}

static PyObject* setFile(PyObject* self, PyObject* args)
{
	//delete g_pPlayer;
	//g_pPlayer = new (std::nothrow) DShowPlayer(PyUnicode_AsUTF8(args));
	//g_pPlayer->Pause();
	PyObject* python_val = Py_BuildValue("");

	return python_val;
}

// Fonction python pour initialiser la vid�o
static PyObject* initPlayer(PyObject* self, PyObject* args)
{
	g_pPlayer = new (std::nothrow) DShowPlayer(PyUnicode_AsUTF8(args));
	g_pPlayer->Pause();
	PyObject* python_val = Py_BuildValue("");

	return python_val;
}

// Fonction python pour envoyer les entr�es claviers
static PyObject* sendInput(PyObject* self, PyObject* args)
{
	ManageInput(*PyUnicode_AsUTF8(args));
	PyObject* python_val = Py_BuildValue("");

	return python_val;
}

// D�finition des fonctions de la librairie
static PyMethodDef VideoPlayerMethods[] =
{
	{"initPlayer", (PyCFunction)initPlayer, METH_O, "Shows the video player."},
	{"sendInput", (PyCFunction)sendInput, METH_O, "Sends input to the video player."},
	{"setFile", (PyCFunction)setFile, METH_O, "Sets the video file used by the video player."},
	{nullptr, nullptr, 0, nullptr}        /* Sentinel */
};

// D�finition du module
static struct PyModuleDef videoplayermodule =
{
	PyModuleDef_HEAD_INIT,
	"Lab3",   /* name of module */
	nullptr, /* module documentation, may be NULL */
	-1,       /* size of per-interpreter state of the module,
				 or -1 if the module keeps state in global variables. */
	VideoPlayerMethods
};

// Initialise le module
PyMODINIT_FUNC PyInit_Lab3(void)
{
	return PyModule_Create(&videoplayermodule);
}
