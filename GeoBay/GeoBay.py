"""Main module."""
import geopandas as gpd
from ipyleaflet import Map as IpyleafletMap, TileLayer, GeoJSON, LayersControl

class Map(IpyleafletMap):
    """
    A custom Map class that extends ipyleaflet.Map with additional functionalities
    for basemap support, layer control, and vector data integration.
    """

    def add_basemap(self, basemap_name: str):
        """
        Adds a basemap to the map.

        Parameters:
        - basemap_name (str): The name of the basemap, e.g., "OpenStreetMap", 
          "Esri.WorldImagery", "OpenTopoMap".
        
        Returns:
        - None
        """
        basemap_urls = {
            "OpenStreetMap": "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            "Esri.WorldImagery": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
            "OpenTopoMap": "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png"
        }

        if basemap_name not in basemap_urls:
            raise ValueError(f"Basemap '{basemap_name}' is not supported.")

        basemap = TileLayer(url=basemap_urls[basemap_name])
        self.add_layer(basemap)

    def add_layer_control(self):
        """
        Adds a layer control widget to manage layers on the map.

        Returns:
        - None
        """
        control = LayersControl()
        self.add_control(control)

    def add_vector(self, vector_data):
        """
        Adds vector data to the map. Supports formats that can be read by GeoPandas 
        (GeoJSON, Shapefile, etc.).

        Parameters:
        - vector_data (str or GeoDataFrame): File path to a vector dataset 
          (Shapefile, GeoJSON) or a GeoPandas GeoDataFrame.

        Returns:
        - None
        """
        if isinstance(vector_data, str):
            gdf = gpd.read_file(vector_data)
        elif isinstance(vector_data, gpd.GeoDataFrame):
            gdf = vector_data
        else:
            raise ValueError("Input must be a file path or a GeoDataFrame.")

        geo_json_data = gdf.__geo_interface__
        geo_json_layer = GeoJSON(data=geo_json_data)
        self.add_layer(geo_json_layer)

# geobay.py

import folium
import geopandas as gpd
from folium.plugins import Draw

class FoliumMap:
    def __init__(self, center=(52.204793, 360.121558), zoom_start=6):
        """
        Initializes a folium map centered at a given location with a specified zoom level.
        
        Parameters:
        center (tuple): Latitude and longitude coordinates for the map center.
        zoom_start (int): The initial zoom level of the map.
        """
        self.map = folium.Map(location=center, zoom_start=zoom_start)

    def add_basemap(self, basemap='OpenStreetMap'):
        """
        Adds a basemap to the folium map.
        
        Parameters:
        basemap (str): The name of the basemap to add (e.g., 'OpenStreetMap', 'Stamen Terrain', etc.).
        """
        basemaps = {
            'OpenStreetMap': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            'Stamen Terrain': 'http://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.jpg',
            'Esri WorldImagery': 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
        }
        folium.TileLayer(tiles=basemaps.get(basemap, basemaps['OpenStreetMap']), attr=basemap).add_to(self.map)

    def add_layer_control(self):
        """
        Adds a layer control widget to the folium map for toggling layers.
        """
        folium.LayerControl().add_to(self.map)

    def add_vector(self, geo_data):
        """
        Adds vector data (GeoJSON or other formats supported by GeoPandas) to the map.
        
        Parameters:
        geo_data (GeoDataFrame or str): A GeoDataFrame or a path to a GeoJSON file.
        """
        if isinstance(geo_data, gpd.GeoDataFrame):
            geo_data = geo_data.to_json()
        folium.GeoJson(geo_data).add_to(self.map)
    
    def show_map(self):
        """
        Displays the folium map in the Jupyter notebook or Python script.
        """
        return self.map
