# DeviceGroupSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**DevicegroupSchemaAuthentication**](DevicegroupSchemaAuthentication.md) |  | [optional] 
**description** | **str** | Description about the device group | [optional] 
**device_group_name** | **str** | Name of the group. Should be of pattern [a-zA-Z][a-zA-Z0-9_-]* | 
**devices** | **list[str]** |  | [optional] 
**logging** | [**DevicegroupSchemaLogging**](DevicegroupSchemaLogging.md) |  | [optional] 
**native_gpb** | [**DevicegroupSchemaNativegpb**](DevicegroupSchemaNativegpb.md) |  | [optional] 
**raw_data** | [**DevicegroupSchemaRawdata**](DevicegroupSchemaRawdata.md) |  | [optional] 
**notification** | [**DevicegroupSchemaNotification**](DevicegroupSchemaNotification.md) |  | [optional] 
**playbooks** | **list[str]** |  | [optional] 
**reports** | **list[str]** |  | [optional] 
**retention_policy** | **str** | Name of the retention policy to be applied | [optional] 
**scheduler** | [**list[DevicegroupSchemaScheduler]**](DevicegroupSchemaScheduler.md) | List of schedulers associated with the playbook instances | [optional] 
**variable** | [**list[DevicegroupSchemaVariable]**](DevicegroupSchemaVariable.md) | Playbook variable configuration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


