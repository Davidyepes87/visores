"""terrenoIA · Sala de visores — arma la carpeta del almacén (GitHub Pages) y catalogo.json.
Cada visor queda en <id>/<vista>.html; la vitrina (Lovable) lee catalogo.json."""
import json, shutil, pathlib, datetime
U = pathlib.Path('/mnt/user-data/uploads/05_BIM_LN'); IG = pathlib.Path('/home/claude/sat_iguana/salida/r05/visores')
OUT = pathlib.Path('/home/claude/visores/repo'); OUT.mkdir(parents=True, exist_ok=True)
EP = '10_Espacio_Publico/02_Proyectos/'; P2 = EP + '02_PAQUETE_02/'
def pq(car, nom, rev):  # parque con diseño y estado actual
    b = f'{car}/04_Visualizaciones/{rev}/'
    return [('diseno', 'Diseño', b + f'Diseno/{nom}_{rev}_Diseno.html'), ('estado-actual', 'Estado actual', b + f'Estado_actual/{nom}_{rev}_Estado_actual.html')]
V = [  # id, título, grupo, lugar, resumen, vistas[(archivo, nombre, ruta origen)], revisión, fecha
 ('la-iguana', 'Gemelo de alerta La Iguaná', 'Gestión del riesgo', 'El Pesebre y Blanquizal, Medellín',
  'Creciente del 09-oct-2026 sobre el terreno 2024: agua por niveles, casas y personas expuestas, sistema de alerta y la propuesta de muros de encauzamiento con su efecto.',
  [('celular', 'Mapa 3D (liviano)', IG / 'Visor_Celular_SAT_La_Iguana_r05.html'), ('mapa', 'Mapa 3D completo', IG / 'Visor_MapLibre_SAT_La_Iguana_r05.html'), ('3d', 'Gemelo 3D (Cesium)', IG / 'Visor_Cesium_SAT_La_Iguana_r05.html')], 'r05', '2026-11-06'),
 ('marinilla', 'Marinilla en 3D', 'Territorio', 'Casco urbano de Marinilla',
  'Construcciones sobre el relieve, espacio público del PMEEP, andenes, caminata a parques y simulación de tránsito de la Calle 28.',
  [('index', 'Mapa 3D', '14_Marinilla/02_Visor/Marinilla_3D.html')], 'r03', '2026-10-30'),
 ('pv-la-madera', 'Paso vial La Madera', 'Vías y movilidad', 'Medellín',
  'Vía y puente modelados en IFC 4.3 sobre el terreno, con el estado actual y el diseño.',
  [('index', 'Vía y puente', EP + 'PV-LA-MADERA/04_Visualizaciones/r09/Visor_PV-LA-MADERA_r09.html')], 'r09', '2026-10-19'),
 ('cola-del-zorro', 'Simulador de tránsito Cola del Zorro', 'Vías y movilidad', 'Medellín',
  'Animación del tránsito sobre la vía en 3D: vehículos, intersecciones y señalización.',
  [('index', 'Simulador', '08_Comercial/Marinilla_2026-10/04_Simulaciones_y_territorio/01_Simulador_de_transito/Simulador_transito_Cola_del_Zorro.html')], 'v06', '2026-10-28'),
 ('lidar-robledo', 'Vía desde nube LIDAR', 'Vías y movilidad', 'Robledo, Medellín',
  'Modelo de la vía reconstruido desde la nube de puntos LIDAR: calzada, andenes y elementos.',
  [('index', 'Vía 3D', '08_Comercial/Marinilla_2026-10/03_Vias/04_Via_desde_nube_LIDAR/Visor_3D_via_desde_LIDAR.html')], 'v03', '2026-09-30'),
 ('jorge-eliecer-gaitan', 'Parque Jorge Eliécer Gaitán', 'Espacio público', 'Comuna 3, Medellín', 'Mejoramiento total del parque: diseño y estado actual en IFC 4.3.',
  pq(EP + 'PA_ZV_JORGE ELIECER GAITAN', 'Jorge_Eliecer_Gaitan', 'r02'), 'r02', '2026-09-24'),
 ('sucre', 'Parque Recreativo Activo Sucre', 'Espacio público', 'Comuna 8, Medellín', 'Diseño y estado actual del parque en IFC 4.3.',
  [('diseno', 'Diseño', EP + 'PA_SUCRE/04_Visualizaciones/r04/Diseno/Sucre_r04_diseno.html'), ('estado-actual', 'Estado actual', EP + 'PA_SUCRE/04_Visualizaciones/r04/Estado_actual/Sucre_r04_estado_actual.html')], 'r04', '2026-09-23'),
 ('el-totazo', 'Zona verde El Totazo', 'Espacio público', 'Comuna 5, Medellín', 'Diseño y estado actual en IFC 4.3.', pq(P2 + 'C5_ZV_EL TOTAZO', 'El_Totazo', 'r02'), 'r02', '2026-09-29'),
 ('barrio-antioquia-1', 'Parque Barrio Antioquia 1', 'Espacio público', 'Comuna 15, Medellín', 'Parque diseñado casi desde cero sobre el estado actual.', pq(EP + '03_PAQUETE_03/C15_BARRIO ANTIOQUIA 1', 'Barrio_Antioquia_1', 'r01'), 'r01', '2026-09-30'),
 ('san-cristobal', 'Parque San Cristóbal', 'Espacio público', 'Corregimiento San Cristóbal, Medellín', 'Diseño completo y estado actual. El diseño es pesado: mejor en computador.',
  [('diseno', 'Diseño', EP + 'PA_SAN CRISTOBAL_C60/04_Visualizaciones/r07/Diseno/San_Cristobal_r07_Diseno.html'), ('estado-actual', 'Estado actual', EP + 'PA_SAN CRISTOBAL_C60/04_Visualizaciones/r07/Estado_actual/San_Cristobal_r07_Estado_actual.html')], 'r07', '2026-10-05'),
 ('las-iguanas', 'Parque Las Iguanas', 'Espacio público', 'Medellín', 'Gemelo del parque sobre el terreno. Pesado: mejor en computador.', [('index', 'Parque', EP + 'PA-LAS-IGUANAS/04_Visualizaciones/r04/Visor_Las_Iguanas_r04.html')], 'r04', '2026-09-22'),
 ('loreto', 'Parque Loreto Sector Nacional', 'Espacio público', 'Medellín', 'Gemelo del parque en IFC 4.3.', [('index', 'Parque', EP + 'PA-LORETO-SECTOR-NACIONAL/04_Visualizaciones/r05/Loreto_visor_r05.html')], 'r05', '2026-09-22'),
 ('la-libertad', 'Parque La Libertad', 'Espacio público', 'Comuna 8, Medellín', 'Modelo de coordinación del parque.', [('index', 'Parque', EP + 'PA-LA-LIBERTAD/04_Visualizaciones/r03/La_Libertad_r03.html')], 'r03', '2026-09-22'),
 ('enrique-olaya', 'Parque Recreativo Versalles (Enrique Olaya Herrera)', 'Espacio público', 'Comuna 3, Medellín', 'Gemelo del parque en IFC 4.3.', [('index', 'Parque', EP + 'PA-ENRIQUE-OLAYA/04_Visualizaciones/r03/Enrique_Olaya_r03.html')], 'r03', '2026-09-23'),
 ('el-salvador', 'Parque El Salvador', 'Espacio público', 'Comuna 9, Medellín', 'Mejoramiento total del parque.', [('index', 'Parque', EP + 'PA_EL_SALVADOR/04_Visualizaciones/r02/El_Salvador_r02.html')], 'r02', '2026-09-23'),
 ('colinas-de-enciso', 'Parque Colinas de Enciso', 'Espacio público', 'Medellín', 'Gemelo del parque en IFC 4.3.', [('index', 'Parque', EP + 'PA_COLINAS DE ENCISO/04_Visualizaciones/r03/Colinas_Enciso_r03.html')], 'r03', '2026-09-23'),
 ('las-estancias', 'Zona verde Urbanización Las Estancias', 'Espacio público', 'Villatina, Comuna 8, Medellín', 'Propuesta nueva y lo existente.',
  [('diseno', 'Propuesta', EP + 'PA_URB_LAS ESTANCIAS/04_Visualizaciones/r03/Nuevo/Las_Estancias_r03_nuevo.html'), ('estado-actual', 'Existente', EP + 'PA_URB_LAS ESTANCIAS/04_Visualizaciones/r03/Existente/Las_Estancias_r03_existente.html')], 'r03', '2026-09-23'),
 ('orografico-el-jardin', 'Parque Orográfico El Jardín', 'Espacio público', 'Medellín', 'Gemelo del parque en IFC 4.3.', [('index', 'Parque', EP + 'PA_LA_OROGRAFICA EL JARDIN/04_Visualizaciones/r03/Orografico_Jardin_r03.html')], 'r03', '2026-09-23'),
 ('terraza-de-la-villa', 'Parque Terraza de la Villa', 'Espacio público', 'Los Mangos, Comuna 8, Medellín', 'Gemelo del parque en IFC 4.3.', [('index', 'Parque', EP + 'PA_RE_TERRAZA DE LA VILLA/04_Visualizaciones/r01/Terraza_Villa_r01.html')], 'r01', '2026-09-23'),
 ('la-ladera', 'Parque La Ladera', 'Espacio público', 'Comuna 8, Medellín', 'Modelo de coordinación del parque.', [('index', 'Parque', EP + 'PA-LA-LADERA/04_Visualizaciones/r04/La_Ladera_r04.html')], 'r04', '2026-09-20'),
 ('esfuerzos-de-la-paz', 'Parque Esfuerzos de la Paz', 'Espacio público', 'Medellín', 'Gemelo del parque en IFC 4.3.', [('index', 'Parque', EP + 'PA-Esfuerzos-de-la-paz/04_Visualizaciones/Esfuerzos_de_la_Paz_r03.html')], 'r03', '2026-09-18'),
 ('libertad-del-grafiti', 'Parque La Libertad del Grafiti', 'Espacio público', 'Medellín', 'Parque con juegos y detalles. Pesado: mejor en computador.', [('index', 'Parque', EP + 'PA-LA-LIBERTAD-DEL-GRAFITI/04_Visualizaciones/Parque_La_Libertad_r05.html')], 'r05', '2026-09-16'),
 ('la-avanzada-2', 'Parque La Avanzada 2', 'Espacio público', 'Comuna 1, Medellín', 'Diseño y estado actual en IFC 4.3.', pq(P2 + 'C1_ZV_LA AVANZADA 2', 'La_Avanzada_2', 'r04'), 'r04', '2026-09-24'),
 ('santa-ines', 'Parque Santa Inés', 'Espacio público', 'Comuna 3, Medellín', 'Diseño y estado actual en IFC 4.3.', pq(P2 + 'C3_PA_ZD_SANTA INÉS', 'Santa_Ines', 'r02'), 'r02', '2026-09-24'),
 ('club-barrial-brasilia', 'Club Barrial Brasilia', 'Espacio público', 'Comuna 4, Medellín', 'Diseño y estado actual.',
  [('diseno', 'Diseño', P2 + 'C4_ZV_CLUB BARRIAL BRASILIA/04_Visualizaciones/r02/Visor_Diseno_r02.html'), ('estado-actual', 'Estado actual', P2 + 'C4_ZV_CLUB BARRIAL BRASILIA/04_Visualizaciones/r02/Visor_Estado_actual_r02.html')], 'r02', '2026-09-24'),
 ('palermo', 'Parque Palermo', 'Espacio público', 'Comuna 4, Medellín', 'Diseño y estado actual en IFC 4.3.', pq(P2 + 'C4_PA_PALERMO', 'Palermo', 'r02'), 'r02', '2026-09-24'),
 ('cataluna', 'Parque Cataluña', 'Espacio público', 'Comuna 9, Medellín', 'Diseño y estado actual en IFC 4.3.', pq(P2 + 'C9_PA_CATALUÑA', 'Cataluna', 'r02'), 'r02', '2026-09-28'),
 ('barrio-de-jesus', 'Parque Barrio de Jesús', 'Espacio público', 'Comuna 9, Medellín', 'Diseño y estado actual en IFC 4.3.', pq(P2 + 'C9_PA_BARRIO DE JESUS', 'Barrio_Jesus', 'r02'), 'r02', '2026-09-29'),
 ('altos-del-pinal', 'Zona verde Altos del Pinal', 'Espacio público', 'Comuna 8, Medellín', 'Diseño y estado actual en IFC 4.3.', pq(P2 + 'C8_ZV_ALTOS DEL PINAL', 'Altos_Pinal', 'r02'), 'r02', '2026-09-29'),
 ('el-salvador-2', 'Zona verde El Salvador 2', 'Espacio público', 'Comuna 9, Medellín', 'Diseño y estado actual en IFC 4.3.', pq(P2 + 'C9_ZV_EL SALVADOR 2', 'El_Salvador_2', 'r01'), 'r01', '2026-09-29'),
 ('ep-zea', 'Parque Francisco Antonio Zea', 'Ejercicios de diseño', 'Castilla, Medellín', 'Primer diseño propio del módulo de espacio público, con la Carrera 65.', [('index', 'Diseño', EP + 'Ejercicios/EP-ZEA/02_Modelos/EP_ZEA_v03_visor.html')], 'v03', '2026-09-07'),
 ('ep-aguacatala', 'Corredor peatonal EAFIT – Aguacatala', 'Ejercicios de diseño', 'El Poblado, Medellín', 'Andén y rampa accesible NTC 4143 hasta la estación Aguacatala.', [('index', 'Corredor', EP + 'Ejercicios/EP-AGUACATALA/02_Modelos/EP_AGUACATALA_v02_visor.html')], 'v02', '2026-09-08'),
 ('ep-ladera', 'Ejercicio La Ladera', 'Ejercicios de diseño', 'Medellín', 'Ejercicio de diseño de espacio público con amoblamiento del catálogo.', [('index', 'Diseño', EP + 'Ejercicios/EP-LADERA/02_Modelos/visor_EP_LADERA.html')], 'v01', '2026-09-05'),
 ('ep-esperanza', 'Ejercicio La Esperanza', 'Ejercicios de diseño', 'Medellín', 'Ejercicio corto de espacio público.', [('index', 'Diseño', EP + 'Ejercicios/EP-ESPERANZA/02_Modelos/visor_EP_ESPERANZA.html')], 'v01', '2026-09-07'),
 ('parqueadero-motos-barbosa', 'Parqueadero de motos en estructura metálica', 'Edificación', 'Barbosa, Antioquia', 'Parqueadero de 150 motos en tres niveles, con rampa, señalización y energía solar.', [('index', 'Modelo 3D', '02_Proyectos/Lote Barbosa/entregas/03_t4_3_niveles_rampa_18_senalizacion/visor_3d.html')], 't4', '2026-10-26'),
 ('valvula-avk-756', 'Válvula de mariposa AVK 756', 'Catálogo BIM', '—', 'Familia paramétrica DN200 generada en IFC4.', [('index', 'Familia', '01_Catalogo/Familias AVK/AVK_756_DN200_visor.html')], 'v01', '2026-08-14'),
 ('silleta-tecnopipe', 'Silleta Tecnopipe 110×32', 'Catálogo BIM', '—', 'Familia de accesorio de tubería generada para el catálogo.', [('index', 'Familia', '01_Catalogo/Familias Tecnopipe/Tecnopipe_Silleta_110x32_visor.html')], 'v01', '2026-10-02'),
]
cat = []
for vid, tit, grp, lugar, res, vistas, rev, fecha in V:
    d = OUT / vid; d.mkdir(exist_ok=True); vs = []
    for arch, nom, src in vistas:
        s = pathlib.Path(src) if isinstance(src, pathlib.Path) else U / src
        shutil.copyfile(s, d / f'{arch}.html'); mb = round(s.stat().st_size / 1e6, 1)
        vs.append({'id': arch, 'nombre': nom, 'url': f'{vid}/{arch}.html', 'mb': mb, 'celular': mb <= 25})
    cat.append({'id': vid, 'titulo': tit, 'grupo': grp, 'lugar': lugar, 'resumen': res, 'revision': rev, 'fecha': fecha,
                'miniatura': f'miniaturas/{vid}.jpg', 'vistas': vs})
json.dump({'actualizado': datetime.date.today().isoformat(), 'base': 'https://davidyepes87.github.io/visores/',
           'autor': 'Ing. David Yepes Builes — terrenoIA', 'visores': cat}, open(OUT / 'catalogo.json', 'w'), ensure_ascii=False, indent=1)
print(len(cat), 'visores,', sum(len(c['vistas']) for c in cat), 'archivos')
