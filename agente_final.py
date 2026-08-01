

# agente/agente_final.py

print("🤖 Iniciando agente final...")

import sys
import os

# ARREGLO: Añadir rutas de forma más robusta
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
servidor_dir = os.path.join(parent_dir, 'servidor-mcp')
print(f"🔍 Buscando servidor en: {servidor_dir}")

# Añadir al path
sys.path.insert(0, servidor_dir)

# Verificar que podemos importar
try:
    from servidor_simple import ServidorBasico
    print("✅ Servidor importado correctamente")
except ImportError as e:
    print(f"❌ Error importando servidor: {e}")
    print("🔧 Creando servidor inline...")
    
    # Si no puede importar, crear el servidor aquí mismo
    class ServidorBasico:
        def __init__(self):
            print("✅ Servidor creado inline")
            self.herramientas = {}
            self.crear_herramientas()

        def crear_herramientas(self):
            print("🛠️ Creando herramientas...")
            
            def buscar_articulos(tema):
                print(f"🔍 Buscando artículos sobre: {tema}")
                articulos = [
                    {
                        "titulo": f"Introducción a {tema}",
                        "autor": "Dr. García",
                        "resumen": f"Este artículo explica los conceptos básicos de {tema}.",
                        "año": 2024
                    },
                    {
                        "titulo": f"Avances en {tema}",
                        "autor": "Prof. López",
                        "resumen": f"Exploramos los últimos avances en el campo de {tema}.",
                        "año": 2023
                    },
                    {
                        "titulo": f"Aplicaciones prácticas de {tema}",
                        "autor": "Dra. Martínez",
                        "resumen": f"Casos de uso reales donde {tema} ha demostrado ser efectivo.",
                        "año": 2024
                    }
                ]
                print(f"✅ Encontrados {len(articulos)} artículos")
                return articulos

            self.herramientas["buscar_articulos"] = buscar_articulos
            print("✅ Herramienta 'buscar_articulos' creada")

        def usar_herramienta(self, nombre, parametros):
            print(f"🔧 Usando herramienta: {nombre}")
            if nombre in self.herramientas:
                herramienta = self.herramientas[nombre]
                resultado = herramienta(parametros)
                print(f"✅ Herramienta ejecutada correctamente")
                return resultado
            else:
                print(f"❌ Herramienta '{nombre}' no encontrada")
                return None

class AgenteArreglado:
    def __init__(self):
        print("🤖 Creando agente...")
        self.servidor = ServidorBasico()
        print("✅ Agente listo")

    def investigar_completo(self, tema):
        """Hace investigación COMPLETA con análisis"""
        print(f"\n🎯 INVESTIGANDO: {tema}")
        print("=" * 50)

        # PASO 1: Buscar artículos
        print("📚 PASO 1: Buscando artículos...")
        articulos = self.servidor.usar_herramienta("buscar_articulos", tema)
        
        if not articulos:
            print("❌ No se encontraron artículos")
            return None

        print(f"✅ Encontrados {len(articulos)} artículos")

        # PASO 2: Mostrar artículos encontrados
        print("\n📋 ARTÍCULOS ENCONTRADOS:")
        for i, articulo in enumerate(articulos, 1):
            print(f"  {i}. {articulo['titulo']}")
            print(f"     Autor: {articulo['autor']} ({articulo['año']})")

        # PASO 3: ANÁLISIS
        print(f"\n🧠 PASO 2: ANALIZANDO DATOS...")
        
        # Contar por años
        años = {}
        for articulo in articulos:
            año = articulo['año']
            años[año] = años.get(año, 0) + 1
        
        print("📊 Análisis por años:")
        for año, cantidad in años.items():
            print(f"  {año}: {cantidad} artículos")

        # Contar por autores
        autores = {}
        for articulo in articulos:
            autor = articulo['autor']
            autores[autor] = autores.get(autor, 0) + 1
        
        print("\n👥 Análisis por autores:")
        for autor, cantidad in autores.items():
            print(f"  {autor}: {cantidad} artículos")

        # Estadísticas generales
        total = len(articulos)
        año_mas_reciente = max(años.keys())
        año_mas_antiguo = min(años.keys())
        
        print(f"\n📈 ESTADÍSTICAS:")
        print(f"  Total artículos: {total}")
        print(f"  Año más reciente: {año_mas_reciente}")
        print(f"  Año más antiguo: {año_mas_antiguo}")
        print(f"  Período cubierto: {año_mas_reciente - año_mas_antiguo + 1} años")

        # PASO 4: CREAR REPORTE
        print(f"\n📝 PASO 3: CREANDO REPORTE...")
        
        reporte = f"""# REPORTE DE INVESTIGACIÓN: {tema.upper()}

## RESUMEN:
- Total de artículos: {total}
- Período: {año_mas_antiguo} - {año_mas_reciente}
- Años cubiertos: {año_mas_reciente - año_mas_antiguo + 1}

## DISTRIBUCIÓN POR AÑOS:
"""
        
        for año, cantidad in años.items():
            porcentaje = (cantidad / total) * 100
            barras = "█" * int(porcentaje / 20)
            reporte += f"- {año}: {cantidad} artículos ({porcentaje:.1f}%) {barras}\n"

        reporte += f"""
## AUTORES:
"""
        for autor, cantidad in autores.items():
            reporte += f"- {autor}: {cantidad} publicaciones\n"

        reporte += f"""
## ARTÍCULOS DETALLADOS:
"""
        for i, articulo in enumerate(articulos, 1):
            reporte += f"""
{i}. {articulo['titulo']}
   Autor: {articulo['autor']}
   Año: {articulo['año']}
   Resumen: {articulo['resumen']}
"""

        reporte += f"""
## CONCLUSIONES:
- El tema "{tema}" tiene {total} artículos en nuestra base
- {'Alta' if total >= 3 else 'Baja'} actividad de investigación
- Publicaciones distribuidas en {len(años)} años diferentes
- Autores más productivos: {', '.join([f"{a} ({c})" for a, c in autores.items()])}
"""

        print("✅ Reporte creado")

        # PASO 5: MOSTRAR REPORTE COMPLETO
        print(f"\n📄 REPORTE COMPLETO:")
        print("=" * 60)
        print(reporte)
        print("=" * 60)

        # PASO 6: OFRECER GUARDAR
        try:
            guardar = input(f"\n💾 ¿Quieres guardar este reporte? (s/n): ").strip().lower()
            if guardar in ['s', 'si', 'sí', 'yes', 'y']:
                nombre_archivo = f"reporte_{tema.replace(' ', '_').replace('/', '_')}.md"
                with open(nombre_archivo, 'w', encoding='utf-8') as f:
                    f.write(reporte)
                print(f"✅ Guardado como: {nombre_archivo}")
            else:
                print("📝 Reporte no guardado")
        except Exception as e:
            print(f"⚠️ Error al guardar: {e}")

        return reporte

def main():
    print("\n🚀 AGENTE DE INVESTIGACIÓN CON ANÁLISIS COMPLETO")
    print("=" * 60)
    print("📋 Instrucciones:")
    print("- Escribe un tema para investigar (ej: 'machine learning')")
    print("- Escribe 'salir' para terminar")
    print("=" * 60)

    try:
        agente = AgenteArreglado()
        
        while True:
            try:
                tema = input(f"\n🎯 ¿Qué tema investigar? ").strip()
                
                if tema.lower() in ['salir', 'exit', 'quit', '']:
                    print("👋 ¡Hasta luego!")
                    break

                if tema:
                    print(f"\n🚀 Perfecto, investigando '{tema}'...")
                    agente.investigar_completo(tema)
                else:
                    print("⚠️ Escribe un tema válido")

            except KeyboardInterrupt:
                print("\n\n👋 ¡Hasta luego!")
                break
            except Exception as e:
                print(f"⚠️ Error inesperado: {e}")
                print("🔄 Continuando...")

    except Exception as e:
        print(f"❌ Error crítico: {e}")
        print("🔧 Verifica que los archivos estén en su lugar")

if __name__ == "__main__":
    main()

Reportes con visualizaciones
